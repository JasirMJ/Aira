from rest_framework import serializers, exceptions
from AiraPanel.models import *
from AiraPanel.serializers import *


class Purchase_Items_relationSerializers(serializers.ModelSerializer):
    product_name = serializers.SerializerMethodField()
    class Meta:
        model = Purchase_Items_relation
        fields = '__all__'

    def get_product_name(self,obj):
        # print(obj)
        obj = Purchase_Items_relation.objects.filter(id=obj.id).first()
        print(obj.product_Id.name)
        return obj.product_Id.name


class ContractViewSerializer(serializers.ModelSerializer):
    items = Purchase_Items_relationSerializers(many=True)
    vendors = CustomerSerializers(many=True)
    class Meta:
        model = PurchaseContracts
        fields = '__all__'

class PurchasePayemetHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchasePayemetHistory
        fields = '__all__'

class PurchaseOrderSerializer(serializers.ModelSerializer):
    items = Purchase_Items_relationSerializers(many=True)
    payement_history = PurchasePayemetHistorySerializer(many=True)
    vendors = CustomerSerializers(many=True)

    class Meta:
        model = PurchaseOrder
        fields = '__all__'