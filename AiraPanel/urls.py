from django.urls import path, include

from AiraPanel import views

urlpatterns = [
    path('', views.index, name="index"),
    path('category/', views.CategoryView.as_view(), name="register-employer"),
    path('unit/', views.UnitView.as_view(), name="register-employer"),
    path('company/', views.SubCategoryView.as_view(), name="register-employer"),
    path('subcategory/', views.CompanyView.as_view(), name="register-employer"),
]
