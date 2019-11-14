import sys

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from AiraPanel.models import *
from AiraPanel.global_variables import *
from product.serializers import *



def index(request):
    return HttpResponse('Welcome to Aira Products , site is under developement')

class ProductView(ListAPIView):
    serializer_class = ProductsSerializers

    def get_queryset(self):
        queryset = Products.objects.all().order_by('-id')

        id = self.request.POST.get('id','')
        if id == '':
            return queryset
        else:
            queryset = Products.objects.filter(id=id).order_by('-id')
            return queryset


    def post(self,request):



        if Products.objects.all().exists():
            last = Products.objects.last().id
            auto_id = 100000
            pdt_id_count = auto_id + last
        else:
            pdt_id_count = 100000

        name = self.request.POST.get('name')
        hsncode = self.request.POST.get('hsncode', 'hsncode')
        hsngrp = self.request.POST.get('hsngrp', 'hsngrp')
        itemname = self.request.POST.get('itemname', 'itemname')
        company_id = self.request.POST.get('company_id', 'company_id')
        category_id = self.request.POST.get('category_id', 'category_id')
        # sub_category_id = self.request.POST.get('sub_category_id', 'sub_category_id')
        unit_id = self.request.POST.get('unit_id', 'unit_id')
        company_id = self.request.POST.get('company_id', '')
        category_id = self.request.POST.get('category_id', '')
        sub_category_id = self.request.POST.get('sub_category_id', '')
        unit_id = self.request.POST.get('unit_id', '')

        if company_id == "" or not company_id:
            msg = "required company_id"
            return Response(
                {
                    MESSAGE: msg,
                    STATUS: False,
                }
            )

        print(INFO, "company_id :", company_id)
        if category_id == "" or not category_id:
            msg = "required category_id"
            return Response(
                {
                    MESSAGE: msg,
                    STATUS: False,
                }
            )
        print(INFO, "category_id :", category_id)
        if sub_category_id == "" or not sub_category_id:
            msg = "required sub_category_id"
            return Response(
                {
                    MESSAGE: msg,
                    STATUS: False,
                }
            )
        print(INFO, "sub_category_id :", sub_category_id)
        if unit_id == "" or not unit_id:
            msg = "required unit_id"
            return Response(
                {
                    MESSAGE: msg,
                    STATUS: False,
                }
            )
        print(INFO, "unit_id :", unit_id)

        if name == "" or not name:
            msg = "required name"
            return Response(
                {
                    MESSAGE: msg,
                    STATUS: False,
                }
            )
        print(INFO, "name :", id)
        try:
            print(INFO,"Adding to DB")
            p_obj = Products()
            p_obj.pdt = 'AIRA'+ str(pdt_id_count)
            p_obj.name = name
            p_obj.hsn_code = hsncode
            p_obj.hsn_group = hsngrp
            p_obj.item_name = itemname



            #
            # # selling rules
            p_obj.mrp = self.request.POST.get('mrp','200')
            p_obj.wholesale = self.request.POST.get('wholesale','200')
            # sp = models.CharField(max_length=12, null=True)
            # retail = models.CharField(max_length=12, null=True)
            # branch = models.CharField(max_length=12, null=True)
            # loading_charge = models.CharField(max_length=12, null=True)
            p_obj.is_active = self.request.POST.get('active',1)





            # # details
            print("p id",p_obj.id)
            p_obj.save()
            print("p id", p_obj.id)

            p_obj.manufaturer.add(Companies.objects.filter(id=company_id).first().id)
            print("Companies :",Companies.objects.filter(id=company_id).first().name)

            p_obj.category.add(Categories.objects.filter(id=category_id).first().id)
            print("Categories :",Categories.objects.filter(id=category_id).first().name)

            p_obj.subcategory.add(SubCategories.objects.filter(id=sub_category_id).first().id)
            print("SubCategories : ",SubCategories.objects.filter(id=sub_category_id).first().name)

            p_obj.unit.add(Units.objects.filter(id=unit_id).first().id)
            print("Units : ",Units.objects.filter(id=unit_id).first().name)





            return Response(
                {
                    STATUS: True,
                    MESSAGE: name + " added to products"
                }
            )

        except Exception as e:
            p_obj.delete()

            return Response(
                {
                    STATUS:False,
                    MESSAGE: str(e),
                    "line_no": format(sys.exc_info()[-1].tb_lineno),
                }
            )

        # common_name = models.CharField(max_length=12, null=True)


        # reorder_level = models.IntegerField(null=True)
        # rack = models.CharField(max_length=12, null=True)
        # # packing = models.CharField(max_length=12, null=True)
        # max_order_level = models.CharField(max_length=12, null=True)
        # tax_group = models.CharField(max_length=12, null=True)
        # tax_schedule = models.CharField(max_length=12, null=True)
        # gst = models.CharField(max_length=12, null=True)
        # sgst = models.CharField(max_length=12, null=True)
        # igst = models.CharField(max_length=12, null=True)
        # cgst = models.CharField(max_length=12, null=True)
        # cess = models.CharField(max_length=12, null=True)
        # additional_cess = models.CharField(max_length=12, null=True)
        # second_name = models.CharField(max_length=12, null=True)



    def put(self,request):
        id = self.request.POST.get('id')
        name = self.request.POST.get('name')
        hsncode = self.request.POST.get('hsncode', 'hsncode')
        hsngrp = self.request.POST.get('hsngrp', 'hsngrp')
        itemname = self.request.POST.get('itemname', 'itemname')
        company_id = self.request.POST.get('company_id', 'company_id')
        category_id = self.request.POST.get('category_id', 'category_id')
        sub_category_id = self.request.POST.get('sub_category_id', 'sub_category_id')
        unit_id = self.request.POST.get('unit_id', 'unit_id')
        company_id = self.request.POST.get('company_id', '')
        category_id = self.request.POST.get('category_id', '')
        sub_category_id = self.request.POST.get('sub_category_id', '')
        unit_id = self.request.POST.get('unit_id', '')

        if id == "" or not id:
            msg = "required id"
            return Response(
                {
                    MESSAGE: msg,
                    STATUS: False,
                }
            )

        print(INFO, "id :", id)

        if company_id == "" or not company_id:
            msg = "required company_id"
            return Response(
                {
                    MESSAGE: msg,
                    STATUS: False,
                }
            )

        print(INFO, "company_id :", company_id)
        if category_id == "" or not category_id:
            msg = "required category_id"
            return Response(
                {
                    MESSAGE: msg,
                    STATUS: False,
                }
            )
        print(INFO, "category_id :", category_id)
        if sub_category_id == "" or not sub_category_id:
            msg = "required sub_category_id"
            return Response(
                {
                    MESSAGE: msg,
                    STATUS: False,
                }
            )
        print(INFO, "sub_category_id :", sub_category_id)
        if unit_id == "" or not unit_id:
            msg = "required unit_id"
            return Response(
                {
                    MESSAGE: msg,
                    STATUS: False,
                }
            )
        print(INFO, "unit_id :", unit_id)

        if name == "" or not name:
            msg = "required name"
            return Response(
                {
                    MESSAGE: msg,
                    STATUS: False,
                }
            )
        print(INFO, "name :", id)
        print(INFO, "Adding to DB")
        p_obj = Products.objects.filter(id=id).first()
        # p_obj.pdt = 'AIRA' + str(pdt_id_count)
        p_obj.name = name
        p_obj.hsn_code = hsncode
        p_obj.hsn_group = hsngrp
        p_obj.item_name = itemname

        #
        # # selling rules
        p_obj.mrp = self.request.POST.get('mrp', '200')
        p_obj.wholesale = self.request.POST.get('wholesale', '200')
        # sp = models.CharField(max_length=12, null=True)
        # retail = models.CharField(max_length=12, null=True)
        # branch = models.CharField(max_length=12, null=True)
        # loading_charge = models.CharField(max_length=12, null=True)
        p_obj.is_active = self.request.POST.get('active', 1)

        # # details
        try:
            p_obj.save()
        except Exception as e:
            return Response(
                {
                    STATUS: False,
                    MESSAGE: str(e),
                }
            )

        # common_name = models.CharField(max_length=12, null=True)
        p_obj.manufaturer.add(Companies.objects.filter(id=company_id).first().id)
        p_obj.category.add(Categories.objects.filter(id=category_id).first().id)
        p_obj.subcategory.add(SubCategories.objects.filter(id=sub_category_id).first().id)
        p_obj.unit.add(Units.objects.filter(id=unit_id).first().id)

        # reorder_level = models.IntegerField(null=True)
        # rack = models.CharField(max_length=12, null=True)
        # # packing = models.CharField(max_length=12, null=True)
        # max_order_level = models.CharField(max_length=12, null=True)
        # tax_group = models.CharField(max_length=12, null=True)
        # tax_schedule = models.CharField(max_length=12, null=True)
        # gst = models.CharField(max_length=12, null=True)
        # sgst = models.CharField(max_length=12, null=True)
        # igst = models.CharField(max_length=12, null=True)
        # cgst = models.CharField(max_length=12, null=True)
        # cess = models.CharField(max_length=12, null=True)
        # additional_cess = models.CharField(max_length=12, null=True)
        # second_name = models.CharField(max_length=12, null=True)
        return Response(
            {
                STATUS: True,
                MESSAGE: name + " updated"
            }
        )
    def delete(self,request):
        id = self.request.POST.get('id')
        delete = self.request.POST.get('delete','')

        if delete == 'delete':
            Products.objects.all().delete()
            return Response(
                {
                    STATUS:True,
                    MESSAGE:"Deleted all products",
                }
            )

        if id == "" or not id:
            msg = "required id"
            return Response(
                {
                    MESSAGE: msg,
                    STATUS: False,
                }
            )

        print(INFO, "id :", id)
        Products.objects.filter(id=id).delete()
        return Response(
            {
                STATUS:True,
                MESSAGE:"Deleted product with id"+id,
            }
        )

