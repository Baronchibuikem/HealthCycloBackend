from django.urls import path, include
from rest_framework import routers
from data.Api_v1.viewsets.requestdata_viewset import RequestDataViewSet
from data.Api_v1.viewsets.submitdata_viewset import SubmitDataViewSet
from data.Api_v1.viewsets.articles_viewset import ArticleViewSet

app_name = "data"

router = routers.DefaultRouter()

router.register('request-data', RequestDataViewSet)
router.register('submit-data', SubmitDataViewSet)
router.register('articles', ArticleViewSet)

urlpatterns = router.urls
