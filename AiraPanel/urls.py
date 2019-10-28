from django.urls import path, include

from AiraPanel import views

urlpatterns = [
    path('', views.index, name="index"),
    path('category/', views.CategoryView.as_view(), name="category"),
    path('unit/', views.UnitView.as_view(), name="unit"),
    path('company/', views.SubCategoryView.as_view(), name="company"),
    path('subcategory/', views.CompanyView.as_view(), name="subcategory"),
    path('customer/', views.CustomerView.as_view(), name="customer"),
]
