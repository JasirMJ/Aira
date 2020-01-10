from django.contrib.auth import authenticate
from rest_framework import serializers, exceptions
from AiraPanel.models import *


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    def validate(self,data):
        print("info ------------------- Authentication started")
        username = data.get('username','')
        password = data.get('password','')
        print("info ------------------- username and password recieved")
        print("info ------------------- username ",username," and password ",password ," recieved")
        if username and password:
            print("info ------------------- username n password forwaring to authnticate")
            user = authenticate(username=username,password=password)
            if user:
                print("info ------------------- authnticated sucessfully")

                if user.is_active:
                    data['user']=user
                else:
                    msg="user is deactivated"
                    raise exceptions.ValidationError(msg)
            else:
                msg="unable to login with given credentials"
                # return Response({'Message':msg})
                raise exceptions.ValidationError(msg)
        else:
            msg ="validation error"

            raise exceptions.ValidationError(msg)
        return data

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'is_active',
            'date_joined',
            'is_staff',
        ]



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

class CounterSerializers(serializers.ModelSerializer):
    class Meta:
        model = Counter
        fields = "__all__"

class BranchSerializers(serializers.ModelSerializer):
    counter_id = CounterSerializers(many=True)
    class Meta:
        model = Branch
        fields = '__all__'

class CompanySerializers(serializers.ModelSerializer):
    branch_id = BranchSerializers(many=True)
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



class RegisterViewSerializer(serializers.ModelSerializer):
    # userid = serializers.CharField(source='user_id')
    user_id = UserSerializers(read_only=True)
    company = CompanySerializers(many=True)
    # company_id = CompanySerializers
    # CompanySerializers =
    # user_id = serializers.SerializerMethodField()
    class Meta:
        model = AiraAuthentication
        fields = '__all__'
        # fields = ['name','userid']