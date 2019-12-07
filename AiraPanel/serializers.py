from rest_framework import serializers, exceptions
from AiraPanel.models import *

class ProductsSerializers(serializers.ModelSerializer):
    # SNIT = SNITUsers()
    # departments = serializers.SerializerMethodField()

    class Meta:
        model = Products
        # fields = ['username', 'email']
        fields = '__all__'

class CategorySerializers(serializers.ModelSerializer):
    # SNIT = SNITUsers()
    # departments = serializers.SerializerMethodField()

    class Meta:
        model = Categories
        # fields = ['username', 'email']
        fields = '__all__'

class CompanySerializers(serializers.ModelSerializer):
    # SNIT = SNITUsers()
    # departments = serializers.SerializerMethodField()

    class Meta:
        model = Companies
        # fields = ['username', 'email']
        fields = '__all__'

class CustomerSerializers(serializers.ModelSerializer):
    # SNIT = SNITUsers()
    # departments = serializers.SerializerMethodField()
    class Meta:
        model = Customers
        # fields = ['username', 'email']
        fields = '__all__'

class UnitSerializers(serializers.ModelSerializer):
    # SNIT = SNITUsers()
    # departments = serializers.SerializerMethodField()

    class Meta:
        model = Units
        # fields = ['username', 'email']
        fields = '__all__'

class SubCategorySerializers(serializers.ModelSerializer):
    # SNIT = SNITUsers()
    # departments = serializers.SerializerMethodField()

    class Meta:
        model = SubCategories
        # fields = ['username', 'email']
        fields = '__all__'

# class ItemsInvoiceSerializers(serializers.ModelSerializer):
#
#     class Meta:
#         model = ItemsInvoice
#         # fields = ['username', 'email']
#         fields = '__all__'

class Items_relationSerializers(serializers.ModelSerializer):

    class Meta:
        model = Items_relation
        # fields = ['username', 'email']
        fields = '__all__'

