from django.urls import path, include

from AiraPanel import views

urlpatterns = [
    path('', views.index, name="index"),
    path('category/', views.CategoryView.as_view(), name="category"),
    path('unit/', views.UnitView.as_view(), name="unit"),
    path('company/', views.CompanyView.as_view(), name="company"),
    path('subcategory/', views.SubCategoryView.as_view(), name="subcategory"),
    path('customer/', views.CustomerView.as_view(), name="customer"),
    path('sample-data/', views.SampleData.as_view(), name="sample-data"),
    path('register/', views.RegisterView.as_view(), name="register"),
    path('login/', views.LoginView.as_view(), name='login'),
    path('aira-users/', views.AiraUser.as_view(), name='users'),
    path('tax/', views.TaxView.as_view(), name='tax'),
    path('map-tax/', views.PdtTaxMappingView.as_view(), name='tax'),
]
