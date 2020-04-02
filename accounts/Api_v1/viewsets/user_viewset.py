# Default Django/Django_Rest Imports
from rest_framework import generics, permissions
from rest_framework.response import Response
from accounts.models import CustomUser
from rest_framework import status, viewsets

# Third party importd
from knox.models import AuthToken

# Custom imports
from accounts.Api_v1.serializers.user_serializer import (GetUserSerializer,
                                                         RegisterSerializer, LoginSerializer)


class RegisterAPIViewset(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": GetUserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class LoginAPIViewset(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user": GetUserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


# class UserAPIViewset(generics.RetrieveAPIView):
#     permission_classes = [permissions.AllowAny,]
#     serializer_class = GetUserSerializer

#     # For getting details of currently login in user
#     # def get_object(self):
#     #     return self.request.user

#     def get_queryset(self):
#         """
#         This view should return a list of all the purchases
#         for the currently authenticated user.
#         """
#         return CustomUser.objects.all()


class UserAPIViewset(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions
    """
    queryset = CustomUser.objects.all()
    serializer_class = GetUserSerializer
