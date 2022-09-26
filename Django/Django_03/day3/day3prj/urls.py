"""day3prj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
import imp
from django.contrib import admin
from django.urls import path
from can0926 import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("is_odd_even/<int:n1>", views.is_odd_even),
    path("calculator/<int:var1>/<int:var2>", views.calculator),
    path("life_ago/", views.life_ago),
    path("life_ago_show/", views.life_ago_show),
    path("lorem_show/", views.lorem_show),
    path("lorem_/", views.lorem_),
]
