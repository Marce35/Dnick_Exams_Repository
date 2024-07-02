"""
URL configuration for ListingsProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls.static import static

from ListingsApp import views
from ListingsProject import settings

urlpatterns = ([
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('listings/add', views.add_listing, name='add_listing'),
    path('listings/<id>/details', views.listing_details, name='view_listing'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
