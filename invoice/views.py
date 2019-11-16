import json
import sys
import traceback
from datetime import timezone, datetime

from django.contrib.sites import requests
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
        # queryset = Invoices.objects.prefetch_related('items').all().order_by('-id')
        queryset = Invoices.objects.all().order_by('-id')
        # queryset = Invoices.objects.raw('SELECT id, customer FROM airapanel_invoices ')
        print(queryset.query)
        return queryset
    def post(self,reqeust):
        try:
            cst_id = self.request.POST.get('cst_id','')
            due_date = self.request.POST.get('due_date', '')
            cmp_id = self.request.POST.get('cmp_id','')
            status = self.request.POST.get('status','posted')
            total_amount = self.request.POST.get('total_amount')
            paid_amount = float(self.request.POST.get('paid_amount','0'))

            items = self.request.POST.get('items','')
            items = json.loads(items)
            # the result is a Python dictionary:
            # ItemsInvoice.objects.raw(
            #     "INSERT INTO airapanel_itemsinvoice (invoiceId, item_price, tax) "
            #     # "VALUES ("'inv_obj.id'",  )"
            #     "VALUES ("'7'","'32'"," '23' ")"
            # )
            # for x in Invoices.objects.raw("SELECT * FROM airapanel_invoices"):
            #     print(x.id)

            inv_obj = Invoices()
            inv_obj.due_date = due_date
            inv_obj.status = status
            inv_obj.total_amount = total_amount
            inv_obj.paid_amount = paid_amount
            inv_obj.customer= cmp_id
            inv_obj.company= cst_id
            cust_name = Customers.objects.filter(id=cst_id).first().name
            cmp_name = Companies.objects.filter(id=cst_id).first().name
            inv_obj.customer_name = cust_name
            inv_obj.company_name = cmp_name
            inv_obj.save()

            print(INFO,"invoice id ",inv_obj.id)

            instance = []
            for item in items:
                print(item['item'], "rs ", item['price'])
                instance.append(
                    ItemsInvoice(
                        invoiceId=inv_obj.id,
                        product_Id=item['item'],
                        item_price=item['price'],
                        tax=item['tax'],
                        # discount=item['discount'],
                        # tax=item['tax'],
                    ),
                )

            print(instance)
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
            ItemsInvoice.objects.bulk_create(instance)
            for x in ItemsInvoice.objects.filter(invoiceId = inv_obj.id):
                inv_obj.items.add(x)

            # obj = ItemsInvoice(obj)
            # obj.save()
            # for x in

            # ItemsInvoice.objects.bulk_create()


            # inv_obj.delete()
            if float(paid_amount) > 0.0 :
                'if any advance amount paid, it will be recorded in payement history'
                print("Advance paid")
                description = 'advance'
                ph_obj = PayemetHistory()
                ph_obj.invoice_id = inv_obj.id
                ph_obj.date_of_payement = inv_obj.created
                ph_obj.amount = paid_amount
                ph_obj.description = description
                ph_obj.save()
                inv_obj.payement_history.add(ph_obj)
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
            inv_obj.delete()
            return Response(
                {
                    STATUS:False,
                    "Excepction":str(e),
                    MESSAGE:"requred cst_id, due_date, cmp_id, status, total_amount, [paid_amount] ",
                }
            )
    def put(self,reqeust):
        try:
            # id = self.request.POST.get('id')

            return Response(
                {
                    STATUS: True,
                    MESSAGE: "Update not available",
                }
            )
        except Exception as e:
            return Response(
                {

                    STATUS:True,
                    "Excpection":str(e),
                    MESSAGE:"Required fields id"
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

class Payement(ListAPIView):
    def get(self,request):
      return Response(
          {
              STATUS:True,
              MESSAGE:"get not allowed",
          }
      )
    def post(self,request):
        try:
            id = self.request.POST.get('id')

            i_obj = Invoices.objects.filter(id=id)
            type = self.request.POST.get('type')
            amount = self.request.POST.get('amount')
            date = self.request.POST.get('date')
            if i_obj.exists():
                msg = "invoice found"

                i_obj = i_obj.first()
                total_amount = i_obj.total_amount
                if i_obj.status == "paid":
                    return Response(
                        {
                            STATUS:True,
                            MESSAGE:"balance_closed",
                        }
                    )
                if amount:
                    print('amount')
                    pending_amount = int(total_amount) - int(i_obj.paid_amount) - int(amount)

                    ph_obj = PayemetHistory()
                    ph_obj.invoice_id = id
                    ph_obj.date_of_payement = date
                    ph_obj.amount = amount



                    if pending_amount <= 0:
                        i_obj.status = "paid"
                        msg = "thank you , you closed the invoice amount"
                    else:
                        i_obj.status = "paritally_paid"
                        msg = "thank you , we expecting your remaning due soon"
                    i_obj.paid_amount = int(i_obj.paid_amount) + int(amount)

                else:
                    print('!amount')
                    pending_amount = int(total_amount) - int(i_obj.paid_amount)

                ph_obj.save()
                i_obj.payement_history.add(ph_obj)
                i_obj.save()
                return Response(
                    {
                        STATUS:True,
                        MESSAGE:msg,
                        "id":i_obj.id,
                        "total_amount":i_obj.total_amount,
                        "paid_amount":i_obj.paid_amount,
                        "pending_amount":pending_amount,

                    }
                )
            return Response(
                {
                    STATUS: True,
                    MESSAGE: "invoice not found",
                }
            )
        except Exception as e:
            return Response(
                {
                    STATUS:True,
                    "Excepction":str(e),
                    # "line_no":traceback.format_exc(),
                    "line_no":format(sys.exc_info()[-1].tb_lineno),
                    MESSAGE:"Invoice not found",
                }
            )

class SendInvoice(ListAPIView):
    def post(self,request):
        id = self.request.POST.get('id')
        i_obj = Invoices.objects.filter(id=id)
        pass




def SendInvoice(mail, username, password):
    SUBJECT = "Codedady Invoice"
    url = "https://api.sendgrid.com/v3/mail/send"
    data = {
        "personalizations": [
            {
                "to": [
                    {
                        "email": mail,
                    }
                ]
            }
        ],
        "from": {
            "email": "aira.admin@no-replay.com"
        },
        "subject": SUBJECT,
        "content": [
            {
                "type": "text/html",
                "value": '''

<html>
    <body><br>
        <br>
        <center>
        <div style="background-color:rgb(241, 241, 241);height: 600px;width: 500px;">
                <div style="float: left;    background-color:rgb(227, 244, 255);    height: 100px;    width: 200px;">address </div>
                <div class="invoice_details" style="float: right;    background-color:rgb(223, 242, 255);    height: 100px;    width: 200px;">invoice number</div>
            <div style="height: 10px;"></div>    

            <div class="items" style="margin-top:100px;    background-color:red;    height: 200px;    width: 500px;">
                items list
                <div style="background-color: wheat;">
                    <div style="display: inline-block;    width: 78px;    background-color: thistle;">
                        si 
                    </div>
                    <div style="display: inline-block;    width: 78px;    background-color: thistle;">
                        item
                    </div>
                    <div style="display: inline-block;    width: 78px;    background-color: thistle;">
                        tax        
                    </div>
                    <div style="display: inline-block;    width: 78px;    background-color: thistle;">
                        price        
                    </div>
                    <div style="display: inline-block;    width: 78px;    background-color: thistle;">
                        qty
                    </div>
                    <div style="display: inline-block;    width: 78px;    background-color: thistle;">
                        total
                    </div>
                </div>

            </div>

    <div style="float: left ;    margin-top:10px;    background-color:green;    height: 50px;    width: 200px;">other details</div>
        </div>
    </center>
    </body>
</html>
                '''

            }
        ]
    }
    headers = {
        'Content-type': 'application/json',
        # 'Accept': 'text/plain',
        'Authorization': 'Bearer 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',
    }
    r = requests.post(url, data=json.dumps(data), headers=headers)
    print(r)


# SendInvoice('sumi.hostcurator@gmail.com', "jasir", "password")