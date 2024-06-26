"""Aira URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.http import HttpResponse
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from Aira import views
from AiraPanel import views as airaPanelView

from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'category', airaPanelView.CategoryView)
# router.register(r'unit', airaPanelView.UnitView)

urlpatterns = [
    # path('airaAdmin', include(router.urls)),
    path('', views.index),
    path('admin/', admin.site.urls),
    path('billing/', include('billing.urls')),
    path('product/', include('product.urls')),
    path('aira/',include('AiraPanel.urls')),
    path('invoice/',include('invoice.urls')),
    path('purchase/',include('purchase.urls')),
    path('account/',include('account.urls')),
    # path('login/',include('purchase.urls')),
]
