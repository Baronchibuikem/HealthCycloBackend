from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import viewsets
from accounts.models import ContactUs, Subscribe
from accounts.Api_v1.serializers.contactus_subscribe_serializer import ContactUsSerializer, SubscribeSerializer


class ContactUsViewSet(viewsets.ModelViewSet):
    '''
    For rendering the serialized fields of the Contact us
    '''
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer
    # permission_classes = (permissions.IsAuthenticated,)
    permission_classes = (permissions.AllowAny,)


class SubscribeViewSet(viewsets.ModelViewSet):
    '''
    For rendering the serialized fields of the Contact us
    '''
    queryset = Subscribe.objects.all()
    serializer_class = SubscribeSerializer
    # permission_classes = (permissions.IsAuthenticated,)
    permission_classes = (permissions.AllowAny,)