from django.contrib.auth import authenticate
from rest_framework import serializers, exceptions
from AiraPanel.models import *

class AccountGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountGroup
        fields = "__all__"

class AccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accounts
        fields = "__all__"

class GeneralLedgersSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralLedgers
        fields = "__all__"