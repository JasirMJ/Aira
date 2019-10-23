from django.urls import path, include

from billing import views

urlpatterns = [
    path('', views.index, name="index"),
    # path('billing/', views.Billing.as_view(), name="billing"),
]
