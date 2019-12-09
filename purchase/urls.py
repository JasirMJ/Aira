from django.urls import path, include

from purchase import views

urlpatterns = [
    # path('', views.index, name="index"),
    # path('', views.PurchaseView.as_view(), name="purchase"),
    path('contract/', views.ContractView.as_view(), name="contract"),
]
