from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import viewsets
from data.models import Articles
from data.Api_v1.serializers.articles_serializers import ArticlesSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    '''
    For rendering the serialized fields of the Contact us
    '''
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer
    # permission_classes = (permissions.IsAuthenticated,)
    permission_classes = (permissions.AllowAny,)

