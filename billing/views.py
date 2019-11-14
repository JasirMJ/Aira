import json

from django.http import HttpResponse
from django.shortcuts import render
from AiraPanel.global_variables import *

# Create your views here.
from requests import Response
from rest_framework.generics import ListAPIView


def index(request):
    return HttpResponse('Welcome to Aira billing , site is under developement')

class Bill(ListAPIView):
    # serializer_class = InvoiceSerializers

    # def get_queryset(self):
    #     queryset = Invoices.objects.all().order_by('-id')
    #     return queryset

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

            # inv_obj = Invoices()
            # inv_obj.due_date = due_date
            # inv_obj.status = status
            # inv_obj.total_amount = total_amount
            # inv_obj.paid_amount = paid_amount
            #
            # inv_obj.save()
            #
            # cmp_obj = Companies.objects.filter(id=cmp_id).first()
            # cst_obj = Customers.objects.filter(id=cst_id).first()
            #
            # inv_obj.customer.add(cst_obj)
            # inv_obj.company.add(cmp_obj)
            #
            # print(INFO,"invoice id ",inv_obj.id)
            #
            # instance = []
            # for item in items:
            #     print(item['item'], "rs ", item['price'])
            #     instance.append(
            #         ItemsInvoice(
            #             invoiceId=inv_obj.id,
            #             product_Id=item['item'],
            #             item_price=item['price'],
            #             tax=item['tax'],
            #             # discount=item['discount'],
            #             # tax=item['tax'],
            #         ),
            #     )

            # print(instance)
            # instance = [
            #     ItemsInvoice(
            #         invoiceId=inv_obj,
            #         product_Id = 32,
            #         item_price='25',
            #         tax='12'
            #     ),
            #     ItemsInvoice(
            #         invoiceId=inv_obj,
            #         product_Id=32,
            #         item_price='30',
            #         tax='11'
            #     ),
            #     ItemsInvoice(
            #         invoiceId=inv_obj,
            #         product_Id=32,
            #         item_price='52',
            #         tax='10'
            #     )
            # ]
            # obj = ItemsInvoice()
            # obj.
            #
            # ItemsInvoice.objects.bulk_create(instance)
            # for x in ItemsInvoice.objects.filter(invoiceId = inv_obj.id):
            #     inv_obj.items.add(x)

            # obj = ItemsInvoice(obj)
            # obj.save()
            # for x in

            # ItemsInvoice.objects.bulk_create()


            # inv_obj.delete()

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

    # def put(self,reqeust):
    #     try:
    #         # id = self.request.POST.get('id')
    #
    #         return Response(
    #             {
    #                 STATUS: True,
    #                 MESSAGE: "Update not available",
    #             }
    #         )
    #     except Exception as e:
    #         return Response(
    #             {
    #
    #                 STATUS:True,
    #                 "Excpection":str(e),
    #                 MESSAGE:"Required fields id"
    #             }
    #         )
    # def delete(self,reqeust):
    #     delete = self.request.POST.get('delete','')
    #     if delete == 'delete':
    #         Invoices.objects.all().delete()
    #     else :
    #         try:
    #             Invoices.objects.filter(id = delete).delete()
    #
    #         except Exception as e:
    #             return Response(
    #                 {
    #                     STATUS: False,
    #                     MESSAGE: "invoice id required (daswqr221)",
    #                 }
    #             )
    #
    #     return Response(
    #         {
    #             STATUS: True,
    #             MESSAGE: "Record deleted",
    #         }
    #     )
