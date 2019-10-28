import json
from datetime import timezone, datetime

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from AiraPanel.models import *
from AiraPanel.global_variables import *
from product.serializers import *
from invoice.serializers import *


def index(request):
    return HttpResponse('Welcome to Aira Products , site is under developement')

class InvoiceView(ListAPIView):
    serializer_class = InvoiceSerializers

    def get_queryset(self):
        queryset = Invoices.objects.all()
        return queryset
    def post(self,reqeust):
        try:

            cst_id = self.request.POST.get('cst_id','')
            due_date = self.request.POST.get('due_date', '')
            cmp_id = self.request.POST.get('cmp_id','')
            status = self.request.POST.get('status','posted')
            total_amount = self.request.POST.get('total_amount')
            paid_amount = self.request.POST.get('paid_amount','0')

            items = self.request.POST.get('items','')

            items = json.loads(items)

            # the result is a Python dictionary:
            for item in items:
                print(item['item'],"rs ",item['price'])


            for x in Invoices.objects.raw("SELECT * FROM airapanel_invoices"):
                print(x.id)


            i_obj = ItemsInvoice()

            inv_obj = Invoices()
            inv_obj.due_date = due_date
            inv_obj.status = status
            inv_obj.total_amount = total_amount
            inv_obj.paid_amount = paid_amount

            inv_obj.save()

            cmp_obj = Companies.objects.filter(id=cmp_id).first()
            cst_obj = Customers.objects.filter(id=cst_id).first()

            inv_obj.customer.add(cst_obj)
            inv_obj.company.add(cmp_obj)


            # ItemsInvoice.objects.raw(
            #     "INSERT INTO airapanel_itemsinvoice (invoiceId, item_price, tax) "
            #     "VALUES ("'inv_obj.id'",  )"
            # )

            inv_obj.delete()

            return Response(
                {
                    STATUS:True,
                    MESSAGE:"New invoice added",
                    # "id": inv_obj.id,
                    # "due_date": due_date,
                    # "status": status,
                    # "total_amount": total_amount,
                    # "paid_amount": paid_amount,
                    # "customer": cst_id,
                    # "company": cmp_id

                }
            )
        except Exception as e:
            # inv_obj.delete()
            return Response(
                {
                    STATUS:False,
                    "Excepction":str(e),
                    MESSAGE:"requred cst_id, due_date, cmp_id, status, total_amount, [paid_amount] ",
                }
            )
    def put(self,reqeust):
        return Response(
            {
                STATUS: True,
                MESSAGE: "",
            }
        )
    def delete(self,reqeust):
        delete = self.request.POST.get('delete','')
        if delete == 'delete':
            Invoices.objects.all().delete()
        else :
            try:
                Invoices.objects.filter(id = delete).delete()

            except Exception as e:
                return Response(
                    {
                        STATUS: False,
                        MESSAGE: "invoice id required (daswqr221)",
                    }
                )

        return Response(
            {
                STATUS: True,
                MESSAGE: "Record deleted",
            }
        )
