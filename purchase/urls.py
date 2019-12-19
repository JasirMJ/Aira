from django.urls import path, include

from purchase import views

urlpatterns = [
    # path('', views.index, name="index"),
    # path('', views.PurchaseView.as_view(), name="purchase"),
    path('contract/', views.ContractView.as_view(), name="contract"),
    path('purchase-order/', views.PurchaseOrderView.as_view(), name="purchase-order"),
    path('create-bill/', views.CreateBill.as_view(), name="create-bill"),
    path('bill-payement/', views.PurchasePayement.as_view(), name="bill-payement"),
]
