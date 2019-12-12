from rest_framework import serializers, exceptions
from AiraPanel.models import *
from AiraPanel.serializers import *


class Purchase_Items_relationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Purchase_Items_relation
        fields = '__all__'



class ContractViewSerializer(serializers.ModelSerializer):
    items = Purchase_Items_relationSerializers(many=True)
    vendors = CustomerSerializers(many=True)
    class Meta:
        model = PurchaseContracts
        fields = '__all__'