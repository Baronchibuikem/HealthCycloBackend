from django.urls import path, include
from accounts.Api_v1.viewsets.user_viewset import RegisterAPIViewset, LoginAPIViewset, UserAPIViewset
from accounts.Api_v1.viewsets.contactus_subscribe_viewset import ContactUsViewSet, SubscribeViewSet
from knox import views as knox_views
from rest_framework import routers

router = routers.DefaultRouter()

router.register('contact-us', ContactUsViewSet)
router.register('subscribe', SubscribeViewSet)
router.register('users', UserAPIViewset)

urlpatterns = [
    path("auth", include('knox.urls')),
    path("auth/register", RegisterAPIViewset.as_view()),
    path("auth/login", LoginAPIViewset.as_view()),    
    # path("auth/user", UserAPIViewset.as_view()),
    path("auth/logout", knox_views.LogoutView.as_view(), name="knox_logout")
]

urlpatterns += router.urls