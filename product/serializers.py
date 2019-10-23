from rest_framework import serializers, exceptions
from AiraPanel.models import Products

class ProductsSerializers(serializers.ModelSerializer):
    # SNIT = SNITUsers()
    # departments = serializers.SerializerMethodField()

    class Meta:
        model = Products
        # fields = ['username', 'email']
        fields = '__all__'