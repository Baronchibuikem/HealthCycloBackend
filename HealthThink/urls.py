"""HealthThink URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_swagger.views import get_swagger_view

#==================================
#DJANGO ADMIN custom
#==================================
admin.site.site_header = "Health Think"
admin.site.site_title = "HealthThink Staff Portal"
admin.site.index_title = "Welcome to HealthThink Staff Portal"

schema_view = get_swagger_view(title='HealthThink Api Documentation')


urlpatterns = [

    # This will take you to the admin interface
    path('admin/', admin.site.urls),

    path('api/v1/account/', include('accounts.urls')),

    # Path for the data app
    path('api/v1/data/', include('data.urls')),

    # This will show you all the available endpoint in this project
    path('doc/', schema_view),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


