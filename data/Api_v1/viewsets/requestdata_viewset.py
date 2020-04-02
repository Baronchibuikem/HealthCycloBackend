from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import viewsets
from data.models import RequestData
from data.Api_v1.serializers.requestdata_serializers import RequestDataSerializer


class RequestDataViewSet(viewsets.ModelViewSet):
    '''
    For rendering the serialized fields of the Contact us
    '''
    queryset = RequestData.objects.all()
    serializer_class = RequestDataSerializer
    # permission_classes = (permissions.IsAuthenticated,)
    permission_classes = (permissions.AllowAny,)

