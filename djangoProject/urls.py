"""
URL configuration for djangoProject project.

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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

import home.views as home_views
import product.views as product_views
from djangoProject import settings

urlpatterns = [
    path('', include('home.urls')),
    path('home/', include('home.urls')),
    path('search/', product_views.search, name='search'),
    path('product/', include('product.urls')),
    path('category/<int:id>/<slug:slug>', product_views.categoryProducts, name="categoryProducts"),
    #blog sayfaları
    path('hakkimizda', home_views.hakkimizda, name = 'hakkimizda'),
    path('referanslar', home_views.referanslar, name = 'hakkimizda'),
    path('iletisim', home_views.iletisim, name = 'hakkimizda'),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
