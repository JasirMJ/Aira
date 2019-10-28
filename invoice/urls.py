
from django.urls import path, include

from invoice import views

urlpatterns = [
    # path('', views.index, name="index"),
    path('', views.InvoiceView.as_view(), name="invoice"),

]
