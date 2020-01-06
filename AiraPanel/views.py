from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from .models import *
from .global_variables import *
from rest_framework.views import APIView
from .serializers import *


def index(request):
    return HttpResponse('Welcome to Aira , site is under developement')

class CategoryView(ListAPIView):
    serializer_class = CategorySerializers

    def get_queryset(self):
        queryset = Categories.objects.all()
        return queryset
    def post(self,request):
        name = self.request.POST.get('name','')
        if name == "" or not name:
            msg = "required name"
            return Response(
                {
                    MESSAGE: msg,
                    STATUS: False,
                }
            )
        print(INFO, "name :", id)

        obj = Categories()
        obj.name = name
        try:
            obj.save()

            return Response(
                {
                    STATUS: True,
                    MESSAGE: "post",
                }
            )
        except Exception as e:
            return Response(
                {
                    STATUS: False,
                    MESSAGE: str(e),
                }
            )
    def put(self,request):
        id = self.request.POST.get('id','')
        name = self.request.POST.get('name', '')

        if name == "" or not name:
            msg = "required name"
            return Response(
                {
                    MESSAGE: msg,
                    STATUS: False,
                }
            )
        print(INFO, "name :", id)

        if id == "" or not id:
            msg = "required id"
            return Response(
                {
                    MESSAGE: msg,
                    STATUS: False,
                }
            )
        print(INFO, "id :", id)

        obj = Categories.objects.filter(id = id).first()
        obj.name = name
        obj.save()

        return Response(
            {
                STATUS: True,
                MESSAGE: "put",
            }
        )

    def delete(self,request):
        id = self.request.POST.get('id','')
        delete = self.request.POST.get('delete','')
        if delete == "delete":
            Categories.objects.all().delete()
        elif not id == '':
            Categories.objects.filter(id=id).delete()
        return Response(
            {
                STATUS: True,
                MESSAGE: "delete",
            }
        )

class UnitView(ListAPIView):
    serializer_class = UnitSerializers

    def get_queryset(self):
        queryset = Units.objects.all()
        return queryset

    def post(self, request):
        name = self.request.POST.get('name', '')
        if name == "" or not name:
            msg = "required name"
            return Response(
                {
                    MESSAGE: msg,
                    STATUS: False,
                }
            )
        print(INFO, "name :", id)

        obj = Units()
        obj.name = name
        try:
            obj.save()

            return Response(
                {
                    STATUS: True,
                    MESSAGE: "post",
                }
            )
        except Exception as e:
            return Response(
                {
                    STATUS: False,
                    MESSAGE: str(e),
                }
            )

    def put(self, request):
        id = self.request.POST.get('id', '')
        name = self.request.POST.get('name', '')

        if name == "" or not name:
            msg = "required name"
            return Response(
                {
                    MESSAGE: msg,
                    STATUS: False,
                }
            )
        print(INFO, "name :", id)

        if id == "" or not id:
            msg = "required id"
            return Response(
                {
                    MESSAGE: msg,
                    STATUS: False,
                }
            )
        print(INFO, "id :", id)

        obj = Units.objects.filter(id=id).first()
        obj.name = name
        obj.save()

        return Response(
            {
                STATUS: True,
                MESSAGE: "put",
            }
        )

    def delete(self, request):
        id = self.request.POST.get('id', '')
        delete = self.request.POST.get('delete', '')
        if delete == "delete":
            Units.objects.all().delete()
        elif not id == '':
            Units.objects.filter(id=id).delete()
        return Response(
            {
                STATUS: True,
                MESSAGE: "delete",
            }
        )

class SubCategoryView(ListAPIView):
    serializer_class = SubCategorySerializers

    def get_queryset(self):
        queryset = SubCategories.objects.all()
        return queryset

    def post(self, request):
        name = self.request.POST.get('name', '')
        if name == "" or not name:
            msg = "required name"
            return Response(
                {
                    MESSAGE: msg,
                    STATUS: False,
                }
            )
        print(INFO, "name :", id)

        obj = SubCategories()
        obj.name = name
        try:
            obj.save()

            return Response(
                {
                    STATUS: True,
                    MESSAGE: "post",
                }
            )
        except Exception as e:
            return Response(
                {
                    STATUS: False,
                    MESSAGE: str(e),
                }
            )

    def put(self, request):
        id = self.request.POST.get('id', '')
        name = self.request.POST.get('name', '')

        if name == "" or not name:
            msg = "required name"
            return Response(
                {
                    MESSAGE: msg,
                    STATUS: False,
                }
            )
        print(INFO, "name :", id)

        if id == "" or not id:
            msg = "required id"
            return Response(
                {
                    MESSAGE: msg,
                    STATUS: False,
                }
            )
        print(INFO, "id :", id)

        obj = SubCategories.objects.filter(id=id).first()
        obj.name = name
        obj.save()

        return Response(
            {
                STATUS: True,
                MESSAGE: "put",
            }
        )

    def delete(self, request):
        id = self.request.POST.get('id', '')
        delete = self.request.POST.get('delete', '')
        if delete == "delete":
            SubCategories.objects.all().delete()
        elif not id == '':
            SubCategories.objects.filter(id=id).delete()
        return Response(
            {
                STATUS: True,
                MESSAGE: "delete",
            }
        )

class CompanyView(ListAPIView):
    serializer_class = CompanySerializers

    def get_queryset(self):
        queryset = Companies.objects.all()
        return queryset

    def post(self, request):
        name = self.request.POST.get('name', '')
        if name == "" or not name:
            msg = "required name"
            return Response(
                {
                    MESSAGE: msg,
                    STATUS: False,
                }
            )
        print(INFO, "name :", id)

        obj = Companies()
        obj.name = name
        try:
            obj.save()

            return Response(
                {
                    STATUS: True,
                    MESSAGE: "post",
                }
            )
        except Exception as e:
            return Response(
                {
                    STATUS: False,
                    MESSAGE: str(e),
                }
            )

    def put(self, request):
        id = self.request.POST.get('id', '')
        name = self.request.POST.get('name', '')

        if name == "" or not name:
            msg = "required name"
            return Response(
                {
                    MESSAGE: msg,
                    STATUS: False,
                }
            )
        print(INFO, "name :", id)

        if id == "" or not id:
            msg = "required id"
            return Response(
                {
                    MESSAGE: msg,
                    STATUS: False,
                }
            )
        print(INFO, "id :", id)

        obj = Companies.objects.filter(id=id).first()
        obj.name = name
        obj.save()

        return Response(
            {
                STATUS: True,
                MESSAGE: "put",
            }
        )

    def delete(self, request):
        id = self.request.POST.get('id', '')
        delete = self.request.POST.get('delete', '')
        if delete == "delete":
            Companies.objects.all().delete()
            return Response(
                {
                    STATUS: True,
                    MESSAGE: "deleted all",
                }
            )
        elif not id == '':
            print(Companies.objects.filter(id=id).delete())
            return Response(
                {
                    STATUS: True,
                    MESSAGE: "deleted 1 item",
                }
            )
        else:
            return Response(
                {
                    STATUS: True,
                    MESSAGE: "deleted nothing",
                }
            )

class CustomerView(ListAPIView):
    serializer_class = CustomerSerializers

    def get_queryset(self):
        queryset = Customers.objects.all()
        return queryset

    def post(self, request):

        name = self.request.POST.get('name', '')

        address = self.request.POST.get('address', '')
        country = self.request.POST.get('country', '')
        state = self.request.POST.get('state', '')
        city_one = self.request.POST.get('city_one', '')
        city_two = self.request.POST.get('city_two', '')
        phone = self.request.POST.get('phone', '')
        mobile = self.request.POST.get('mobile', '')
        job_position = self.request.POST.get('job_position', '')
        email = self.request.POST.get('email', '')

        if(Customers.objects.exists()):
            aira_code = 'CUST'+str(Customers.objects.last().id+1)
            print(aira_code)
        else:
            aira_code = 'CUST'+'1'
        print(aira_code)

        if name == "" or not name:
            msg = "required name"
            return Response(
                {
                    MESSAGE: msg,
                    STATUS: False,
                }
            )
        print(INFO, "name :", id)

        obj = Customers()
        obj.name = name
        obj.aira_code = aira_code
        obj.address = address
        obj.country = country
        obj.state = state
        obj.city_one = city_one
        obj.city_two = city_two
        obj.phone = phone
        obj.mobile = mobile
        obj.job_position = job_position
        obj.email = email

        try:
            obj.save()

            return Response(
                {
                    STATUS: True,
                    MESSAGE: "post",
                }
            )
        except Exception as e:
            return Response(
                {
                    STATUS: False,
                    MESSAGE: str(e),
                }
            )

    def put(self, request):
        id = self.request.POST.get('id', '')
        name = self.request.POST.get('name', '')

        if name == "" or not name:
            msg = "required name"
            return Response(
                {
                    MESSAGE: msg,
                    STATUS: False,
                }
            )
        print(INFO, "name :", id)

        if id == "" or not id:
            msg = "required id"
            return Response(
                {
                    MESSAGE: msg,
                    STATUS: False,
                }
            )
        print(INFO, "id :", id)

        obj = Customers.objects.filter(id=id).first()
        obj.name = name
        obj.save()

        return Response(
            {
                STATUS: True,
                MESSAGE: "put",
            }
        )

    def delete(self, request):
        id = self.request.POST.get('id', '')
        delete = self.request.POST.get('delete', '')
        if delete == "delete":
            Customers.objects.all().delete()
        elif not id == '':
            Customers.objects.filter(id=id).delete()
        return Response(
            {
                STATUS: True,
                MESSAGE: "delete",
            }
        )



class SampleData(ListAPIView):
    def post(self,request):
        companies_data = ['facebook','google','tata','codedady','bismi']
        units_data = ['liter','pic','kg','g']
        category_data = ['software','hardware','vehicle','developement','food']
        subcategory_data = ['android','ram','suv','webdevelopement','biriyani']
        customer_data = ['jasir','fayis','rohit','sali','salman','anas']
        product_data = ['ecommerce','ram_8gb','tesla','chicken','ajmeer biriyani']

        with transaction.atomic():
            Products.objects.all().delete()
            Categories.objects.all().delete()
            Customers.objects.all().delete()
            SubCategories.objects.all().delete()
            Units.objects.all().delete()
            Companies.objects.all().delete()

            comp_instance = []
            for company in companies_data:
                print("Companies :",company)
                comp_instance.append(
                    Companies(
                        name=company
                    )
                )
            units_instance = []
            for unit in units_data:
                print("unit :",unit)

                units_instance.append(
                    Units(
                        name=unit
                    )
                )

            cat_instance = []
            for category in category_data:
                print("category :",category)
                cat_instance.append(
                    Categories(
                        name=category
                    )
                )

            subcategory_instance = []
            for subcategory in subcategory_data:
                print("subcategory :",subcategory)
                subcategory_instance.append(
                    SubCategories(
                        name=subcategory
                    )
                )

            customer_instance = []
            for customer in customer_data:
                print("customer :",customer)
                customer_instance.append(
                    Customers(
                        name=customer
                    )
                )

            Companies.objects.bulk_create(comp_instance)
            Units.objects.bulk_create(units_instance)
            Categories.objects.bulk_create(cat_instance)
            SubCategories.objects.bulk_create(subcategory_instance)
            Customers.objects.bulk_create(customer_instance)

            product_instance = []
            p_obj1 = Products(
                name = 'gpay',
                is_active=1
            )
            p_obj1.save()
            p_obj1.manufaturer.add(Companies.objects.filter(name='facebook').first().id)
            p_obj1.category.add(Categories.objects.filter(name='software').first().id)
            p_obj1.subcategory.add(SubCategories.objects.filter(name='webdevelopement').first().id)
            p_obj1.unit.add(Units.objects.filter(name='pic').first().id)

            p_obj2 = Products(
                name = 'playstore',
                is_active=1
            )
            p_obj2.save()
            p_obj2.manufaturer.add(Companies.objects.filter(name='google').first().id)
            p_obj2.category.add(Categories.objects.filter(name='developement').first().id)
            p_obj2.subcategory.add(SubCategories.objects.filter(name='android').first().id)
            p_obj2.unit.add(Units.objects.filter(name='pic').first().id)

            p_obj3 = Products(
                name='mandhi',
                is_active=1
            )
            p_obj3.save()

            p_obj3.manufaturer.add(Companies.objects.filter(name='bismi').first().id)
            p_obj3.category.add(Categories.objects.filter(name='food').first().id)
            p_obj3.subcategory.add(SubCategories.objects.filter(name='biriyani').first().id)
            p_obj3.unit.add(Units.objects.filter(name='pic').first().id)

            p_obj4 = Products(
                name='rab 8gb',
                is_active=1
            )
            p_obj4.save()
            p_obj4.manufaturer.add(Companies.objects.filter(name='bismi').first().id)
            p_obj4.category.add(Categories.objects.filter(name='hardware').first().id)
            p_obj4.subcategory.add(SubCategories.objects.filter(name='ram').first().id)
            p_obj4.unit.add(Units.objects.filter(name='pic').first().id)

        return Response(
            {
                MESSAGE:"Sucess",
                STATUS:True
            }
        )

class RegisterView(ListAPIView):
    serializer_class = RegisterViewSerializer

    def get_queryset(self):
        qs = AiraAuthentication.objects.all()
        return qs

    def post(self,request):
        return Response(
            {
                STATUS:True,
                MESSAGE:"Sucess",
            }
        )
