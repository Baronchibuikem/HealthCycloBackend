from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import viewsets
from data.models import SubmitData
from data.Api_v1.serializers.submitdata_serializers import SubmitDataSerializer
from rest_framework.parsers import FormParser, MultiPartParser

class SubmitDataViewSet(viewsets.ModelViewSet):
    '''
    For rendering the serialized fields of the Contact us
    '''
    queryset = SubmitData.objects.all()
    serializer_class = SubmitDataSerializer
    # permission_classes = (permissions.IsAuthenticated,)
    permission_classes = (permissions.AllowAny,)
    # parser_classes = (MultiPartParser, FormParser,)