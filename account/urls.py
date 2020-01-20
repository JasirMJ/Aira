from django.urls import path, include

from account import views

urlpatterns = [
    path('', views.index, name="index"),
    path('group/', views.AccountGroupView.as_view(), name="account-group"),
    path('accounts/', views.AccountsView.as_view(), name="accounts"),
    path('ledger/', views.GeneralLedgerView.as_view(), name="accounts"),
]
