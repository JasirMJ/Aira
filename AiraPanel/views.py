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
        elif not id == '':
            Companies.objects.filter(id=id).delete()
        return Response(
            {
                STATUS: True,
                MESSAGE: "delete",
            }
        )

class CustomerView(ListAPIView):
    serializer_class = CustomerSerializers

    def get_queryset(self):
        queryset = Customers.objects.all()
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

        obj = Customers()
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








