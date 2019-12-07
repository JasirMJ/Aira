
from django.urls import path, include

from invoice import views

urlpatterns = [
    # path('', views.index, name="index"),
    path('', views.InvoiceView.as_view(), name="invoice"),
    path('sales/', views.SalesView.as_view()),
    path('payements/', views.Payement.as_view(), name="invoice"),
    # path('invoice_action/', views.InvoiceAction.as_view()),
    path('test/', views.Test.as_view()),


]
