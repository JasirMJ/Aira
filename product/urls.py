from django.urls import path, include

from product import views

urlpatterns = [
    path('', views.index, name="index"),
    path('product/', views.ProductView.as_view(), name="register-employer"),

]
