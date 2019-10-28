from rest_framework import serializers, exceptions
from AiraPanel.models import *
from AiraPanel.serializers import *


class InvoiceSerializers(serializers.ModelSerializer):
    # SNIT = SNITUsers()
    # departments = serializers.SerializerMethodField()

    class Meta:
        model = Invoices
        # fields = ['username', 'email']
        fields = '__all__'