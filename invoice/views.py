import json
import sys
import traceback
from datetime import timezone, datetime

import pdfkit
from django.contrib.sites import requests
from django.db import transaction
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
import requests


# Create your views here.
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from AiraPanel.models import *
from AiraPanel.global_variables import *
from product.serializers import *
from invoice.serializers import *

'''<sendgrid>'''
import base64
import os
import json
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (
    Mail, Attachment, FileContent, FileName,
    FileType, Disposition, ContentId)
try:
    # Python 3
    import urllib.request as urllib
except ImportError:
    # Python 2
    import urllib2 as urllib

import os
import json
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
'''</sendgrid>'''


def index(request):
    return HttpResponse('Welcome to Aira Products , site is under developement')




class SalesView(ListAPIView):
    serializer_class = SalesSerializers

    def get_queryset(self):
        queryset = Sales.objects.all().order_by('-id')
        return queryset

    def post(self,request):
        cst_id = self.request.POST.get('cst_id', '')
        due_date = self.request.POST.get('due_date', '')
        cmp_id = self.request.POST.get('cmp_id', '')
        total_amount = self.request.POST.get('total_amount')
        # paid_amount = float(self.request.POST.get('paid_amount', '0'))

        items = self.request.POST.get('items', '')
        items = json.loads(items)

        action = self.request.POST.get('action')

        # bill_type = self.request.POST.get('bill_type', '')

        if action == "" or not action:
            return Response(
                {
                    STATUS: False,
                    MESSAGE: "Required 'action' ",
                    CODE: "d1e23rf1",
                }
            )

        sale_obj = Sales()
        sale_obj.due_date = due_date
        sale_obj.total_amount = total_amount
        sale_obj.customer = Customers.objects.filter(id=cst_id).first()
        sale_obj.company = Companies.objects.filter(id=cmp_id).first()

        history_obj = History()



        quotation = "Quotation"
        nothing_to_invoice = "Noting to invoice"
        cancelled = "Cancelled"
        sale_order = "Sale order"
        to_invoice = "To invoice"
        quotation_send = "Quotation send"


        if action == "quotation_save":
            sale_obj.status = quotation
            sale_obj.invoice_status = to_invoice

            history_obj.type = "quotation"
            history_obj.modified_at = datetime.now()
            history_obj.description = "quotation saved"

        elif action == "quotation_send_email":
            sale_obj.status = quotation_send
            sale_obj.invoice_status = nothing_to_invoice

            history_obj.type = "quotation"
            history_obj.modified_at = datetime.now()
            history_obj.description = "quotation send as email"

        elif action == "quotation_cancell":
            sale_obj.status = cancelled
            sale_obj.invoice_status = nothing_to_invoice

            history_obj.type = "quotation"
            history_obj.modified_at = datetime.now()
            history_obj.description = "quotation cancelled"

        elif action == "quotation_confirm":
            sale_obj.status = sale_order
            sale_obj.invoice_status = to_invoice

            history_obj.type = "quotation"
            history_obj.modified_at = datetime.now()
            history_obj.description = "quotation confirmed"

        elif action == "sale_save":
            sale_obj.status = sale_order
            sale_obj.invoice_status = to_invoice

            history_obj.type = "saleorder"
            history_obj.modified_at = datetime.now()
            history_obj.description = "saleorder saved"

        elif action == "sale_confirm":
            sale_obj.status = sale_order
            sale_obj.invoice_status = to_invoice

            history_obj.type = "saleorder"
            history_obj.modified_at = datetime.now()
            history_obj.description = "saleorder created"

        elif action == "sale_cancell":
            sale_obj.status = ''
            sale_obj.invoice_status = ''

            history_obj.type = "saleorder"
            history_obj.modified_at = datetime.now()
            history_obj.description = "saleorder cancelled"

        elif action == "sale_send_email":
            sale_obj.status = ''
            sale_obj.invoice_status = ''

            history_obj.type = "saleorder"
            history_obj.modified_at = datetime.now()
            history_obj.description = "saleorder send as email"

        else :
            return Response(
                {
                    STATUS:False,
                    MESSAGE:"Required action",
                }
            )

        try:
            # print("before :",sale_obj.id)
            #
            # print("after :", sale_obj.id)
            # sale_obj.save()
            # history_obj.sales_id = sale_obj.id
            # print(sale_obj.id)
            #
            # history_obj.save()
            #
            # sale_obj.history.add(history_obj)

            with transaction.atomic():
                # This code executes inside a transaction.
                print("after :", sale_obj.id)
                sale_obj.save()
                history_obj.sales_id = sale_obj.id
                print(sale_obj.id)
                history_obj.save()
                sale_obj.history.add(history_obj)

            print("sale obj saved")
            print(INFO,"invoice id ",sale_obj.id)
            instance = []
            for item in items:
                # print(Products.objects.filter(id=item['id']).first())
                print(item['id'], "rs ", item['price'])
                instance.append(
                    Items_relation(
                        sales_id=sale_obj.id,
                        product_Id=Products.objects.filter(id=item['id']).first(),
                        item_price=item['price'],
                        tax=item['tax'],
                    ),
                )

            print(instance)

            Items_relation.objects.bulk_create(instance)

            for x in Items_relation.objects.filter(sales_id = sale_obj.id):
                sale_obj.items.add(x)

            return Response(
                {
                    STATUS:True,
                    MESSAGE:"New quotaion/sales added",
                }
            )
        except Exception as e:
            print("Excepction :"+str(e)+ " Line no :"+ str(format(sys.exc_info()[-1].tb_lineno)))
            if sale_obj:
                sale_obj.delete()

            return Response(
                {
                    STATUS:False,
                    "Excepction":str(e),
                    "Line no":str(format(sys.exc_info()[-1].tb_lineno)),
                    MESSAGE:"requred cst_id, due_date, cmp_id, status, total_amount, [paid_amount] ",
                }
            )

    def put(self,request):

        saleid = self.request.POST.get('saleid', '')
        cst_id = self.request.POST.get('cst_id', '')
        due_date = self.request.POST.get('due_date', '')
        cmp_id = self.request.POST.get('cmp_id', '')
        total_amount = self.request.POST.get('total_amount')
        # paid_amount = float(self.request.POST.get('paid_amount', '0'))

        items = self.request.POST.get('items', '')
        items = json.loads(items)

        action = self.request.POST.get('action')

        # bill_type = self.request.POST.get('bill_type', '')
        if saleid == "" or not saleid:
            return Response(
                {
                    STATUS: False,
                    MESSAGE: "Required 'saleid' ",
                    CODE: "d1e23rfasd1",
                }
            )

        if action == "" or not action:
            return Response(
                {
                    STATUS: False,
                    MESSAGE: "Required 'action' ",
                    CODE: "d1e23rf1",
                }
            )

        sale_obj = Sales.objects.filter(id = saleid).first()
        if not sale_obj:
            return Response(
                {
                    STATUS:False,
                    MESSAGE:"No matching object found"
                }
            )

        sale_obj.due_date = due_date
        sale_obj.total_amount = total_amount
        sale_obj.customer = Customers.objects.filter(id=cst_id).first()
        sale_obj.company = Companies.objects.filter(id=cmp_id).first()

        history_obj = History()

        quotation = "Quotation"
        nothing_to_invoice = "Noting to invoice"
        cancelled = "Cancelled"
        sale_order = "Sale order"
        to_invoice = "To invoice"
        quotation_send = "Quotation send"
        fully_invoiced = "Fully invoiced"

        if action == "quotation_edit":
            # sale_obj.status = quotation
            # sale_obj.invoice_status = to_invoice

            history_obj.type = "quotation"
            history_obj.modified_at = datetime.now()
            history_obj.description = "quotation edited"

        elif action == "quotation_confirm":
            # sale_obj.status = quotation_send
            # sale_obj.invoice_status = nothing_to_invoice

            history_obj.type = "saleorder"
            history_obj.modified_at = datetime.now()
            history_obj.description = "Nothing to invoice"

        elif action == "create_invoice":
            sale_obj.status = sale_order
            sale_obj.invoice_status = fully_invoiced

            history_obj.type = "invoice"
            history_obj.modified_at = datetime.now()
            history_obj.description = "saleorder to invoice"

            # obj = Invoices()
            invoice_obj = Invoices()
            invoice_obj.due_date = due_date
            invoice_obj.type = "invoice"
            invoice_obj.total_amount = total_amount
            invoice_obj.customer = Customers.objects.filter(id=cst_id).first()
            invoice_obj.company = Companies.objects.filter(id=cmp_id).first()

            items_obj = Items_relation.objects.filter(sales_id=sale_obj.id)
            print("items_obj :",items_obj)



            # print("items_obj :",items_obj)
        else:
            return Response(
                {
                    STATUS: False,
                    MESSAGE: "Required action",
                    CODE:"qwdwqdqwa"
                }
            )

        try:

            with transaction.atomic():



                # This code executes inside a transaction.
                print("after :", sale_obj.id)
                sale_obj.save()
                invoice_obj.save()
                for x in items_obj:
                    # x.invoice_id = invoice_obj.id
                    invoice_obj.items.add(x)

                Items_relation.objects.filter(sales_id=sale_obj.id).update(invoice_id=invoice_obj.id)

                history_obj.sales_id = sale_obj.id
                history_obj.invoice_id = invoice_obj.id

                print(sale_obj.id)
                history_obj.save()

                sale_obj.history.add(history_obj)

                # invoice_obj.items.add(sale_obj.items.id)

            print("sale obj saved")
            print(INFO, "invoice id ", sale_obj.id)


            return Response(
                {
                    STATUS: True,
                    MESSAGE: "Quotaion/Sales updated",
                }
            )
        except Exception as e:
            print("Excepction :" + str(e) + " Line no :" + str(format(sys.exc_info()[-1].tb_lineno)))
            if sale_obj:
                sale_obj.delete()

            return Response(
                {
                    STATUS: False,
                    "Excepction": str(e),
                    "Line no": str(format(sys.exc_info()[-1].tb_lineno)),
                    MESSAGE: "requred cst_id, due_date, cmp_id, status, total_amount, [paid_amount] ",
                }
            )

class InvoiceView(ListAPIView):
    serializer_class = InvoiceSerializers
    def get_queryset(self):
        queryset = Invoices.objects.all().order_by('-id')

        return queryset

    def post(self, request):
        cst_id = self.request.POST.get('cst_id', '')
        due_date = self.request.POST.get('due_date', '')
        cmp_id = self.request.POST.get('cmp_id', '')
        total_amount = self.request.POST.get('total_amount')
        paid_amount = float(self.request.POST.get('paid_amount', '0'))
        type = self.request.POST.get('type', 'invoice')

        items = self.request.POST.get('items', '')
        items = json.loads(items)
        action = self.request.POST.get('action')

        if action == "" or not action:
            return Response(
                {
                    STATUS: False,
                    MESSAGE: "Required 'action' ",
                    CODE: "d1e23rf1",
                }
            )

        invoice_obj = Invoices()
        invoice_obj.type = type
        invoice_obj.due_date = due_date
        invoice_obj.total_amount = total_amount
        invoice_obj.paid_amount = paid_amount
        invoice_obj.customer = Customers.objects.filter(id=cst_id).first()
        invoice_obj.company = Companies.objects.filter(id=cmp_id).first()

        history_obj = History()

        # quotation = "Quotation"
        # nothing_to_invoice = "Noting to invoice"
        # cancelled = "Cancelled"
        # sale_order = "Sale order"
        # to_invoice = "To invoice"
        # quotation_send = "Quotation send"

        draft = "draft"
        post = "posted"

        if action == "invoice_save":
            invoice_obj.status = draft
            # invoice_obj.invoice_status = draft

            history_obj.type = "invoice"
            history_obj.modified_at = datetime.now()
            history_obj.description = "invoice saved"

        elif action == "invoice_post":
            invoice_obj.status = post
            # invoice_obj.invoice_status = post

            history_obj.type = "invoice"
            history_obj.modified_at = datetime.now()
            history_obj.description = "invoice posted"

        else:
            return Response(
                {
                    STATUS: False,
                    MESSAGE: "Required invoice action < invoice_save, invoice_post>]",
                    CODE:"asddqwcaa",
                }
            )

        try:

            # if float(paid_amount) > 0.0 :
            #     'if any advance amount paid, it will be recorded in payement history'
            #     print("Advance paid")
            #     description = 'advance'
            #     # print(datetime.now())
            #     ph_obj = PayemetHistory()
            #     ph_obj.invoice_id = invoice_obj.id
            #     ph_obj.date_of_payement = datetime.now()
            #     ph_obj.amount = paid_amount
            #     ph_obj.description = description
            #     ph_obj.save()
            #     invoice_obj.payement_history.add(ph_obj)

            with transaction.atomic():
                # This code executes inside a transaction.



                invoice_obj.save()
                print("Invoice saved")
                history_obj.invoice_id = invoice_obj.id
                print(invoice_obj.id)
                history_obj.save()
                print("History saved")
                invoice_obj.history.add(history_obj)
                print("Invoice added to history")

                # if float(paid_amount) > 0.0:
                #     'if any advance amount paid, it will be recorded in payement history'
                #     print("Advance paid")
                #     description = 'advance'
                #     ph_obj = PayemetHistory()
                #     ph_obj.invoice_id = invoice_obj.id
                #     ph_obj.date_of_payement = invoice_obj.created
                #     ph_obj.amount = paid_amount
                #     ph_obj.description = description
                #     ph_obj.save()
                #     print("advance payement saved to payement history")
                #     invoice_obj.payement_history.add(ph_obj)
                #     print("Invoice added to payement history")

            print(INFO, "invoice id ", invoice_obj.id)
            instance = []
            for item in items:
                # print(Products.objects.filter(id=item['id']).first())
                print(item['id'], "rs ", item['price'])
                instance.append(
                    Items_relation(
                        invoice_id=invoice_obj.id,
                        product_Id=Products.objects.filter(id=item['id']).first(),
                        item_price=item['price'],
                        tax=item['tax'],
                    ),
                )

            print(instance)

            Items_relation.objects.bulk_create(instance)
            print("items added to items_relation")

            for x in Items_relation.objects.filter(sales_id=invoice_obj.id):
                invoice_obj.items.add(x)
            print("invoice maped with items")

            return Response(
                {
                    STATUS: True,
                    MESSAGE: "New invoice added",
                }
            )
        except Exception as e:
            print("Excepction :" + str(e) + " Line no :" + str(format(sys.exc_info()[-1].tb_lineno)))
            if invoice_obj:
                invoice_obj.delete()
                print("invoice_obj deleted")

            if history_obj:
                history_obj.delete()
                print("history_obj deleted")

            return Response(
                {
                    STATUS: False,
                    "Excepction": str(e),
                    "Line no": str(format(sys.exc_info()[-1].tb_lineno)),
                    MESSAGE: "requred cst_id, due_date, cmp_id, status, total_amount, [paid_amount] ",
                }
            )

    def put(self, request):
        return Response(
            "Currently unavailable"
        )
        saleid = self.request.POST.get('saleid', '')
        cst_id = self.request.POST.get('cst_id', '')
        due_date = self.request.POST.get('due_date', '')
        cmp_id = self.request.POST.get('cmp_id', '')
        total_amount = self.request.POST.get('total_amount')
        # paid_amount = float(self.request.POST.get('paid_amount', '0'))

        type = float(self.request.POST.get('type', 'invoice'))

        items = self.request.POST.get('items', '')
        items = json.loads(items)

        action = self.request.POST.get('action')

        # bill_type = self.request.POST.get('bill_type', '')
        if saleid == "" or not saleid:
            return Response(
                {
                    STATUS: False,
                    MESSAGE: "Required 'saleid' ",
                    CODE: "d1e23rfasd1",
                }
            )

        if action == "" or not action:
            return Response(
                {
                    STATUS: False,
                    MESSAGE: "Required 'action' ",
                    CODE: "d1e23rf1",
                }
            )

        sale_obj = Sales.objects.filter(id=saleid).first()
        if not sale_obj:
            return Response(
                {
                    STATUS: False,
                    MESSAGE: "No matching object found"
                }
            )

        sale_obj.due_date = due_date
        sale_obj.total_amount = total_amount
        sale_obj.customer = Customers.objects.filter(id=cst_id).first()
        sale_obj.company = Companies.objects.filter(id=cmp_id).first()

        history_obj = History()

        quotation = "Quotation"
        nothing_to_invoice = "Noting to invoice"
        cancelled = "Cancelled"
        sale_order = "Sale order"
        to_invoice = "To invoice"
        quotation_send = "Quotation send"
        fully_invoiced = "Fully invoiced"

        if action == "quotation_edit":
            # sale_obj.status = quotation
            # sale_obj.invoice_status = to_invoice

            history_obj.type = "quotation"
            history_obj.modified_at = datetime.now()
            history_obj.description = "quotation edited"

        elif action == "quotation_confirm":
            # sale_obj.status = quotation_send
            # sale_obj.invoice_status = nothing_to_invoice

            history_obj.type = "saleorder"
            history_obj.modified_at = datetime.now()
            history_obj.description = "Nothing to invoice"

        elif action == "create_invoice":
            sale_obj.status = sale_order
            sale_obj.invoice_status = fully_invoiced

            history_obj.type = "quotation"
            history_obj.modified_at = datetime.now()
            history_obj.description = "quotation cancelled"
        else:
            return Response(
                {
                    STATUS: False,
                    MESSAGE: "Required action",
                    CODE: "qwdwqdqwa"
                }
            )

        try:

            with transaction.atomic():
                # This code executes inside a transaction.
                print("after :", sale_obj.id)
                sale_obj.save()
                history_obj.sales_id = sale_obj.id
                print(sale_obj.id)
                history_obj.save()
                sale_obj.history.add(history_obj)

            print("sale obj saved")
            print(INFO, "invoice id ", sale_obj.id)

            return Response(
                {
                    STATUS: True,
                    MESSAGE: "Quotaion/Sales updated",
                }
            )
        except Exception as e:
            print("Excepction :" + str(e) + " Line no :" + str(format(sys.exc_info()[-1].tb_lineno)))
            if sale_obj:
                sale_obj.delete()

            return Response(
                {
                    STATUS: False,
                    "Excepction": str(e),
                    "Line no": str(format(sys.exc_info()[-1].tb_lineno)),
                    MESSAGE: "requred cst_id, due_date, cmp_id, status, total_amount, [paid_amount] ",
                }
            )


class InvoiceViewOld(ListAPIView):
    # serializer_class = InvoiceSerializers

    def get_queryset(self):


        type = self.request.GET['type']
        queryset = Invoices.objects.all().order_by('-id')
        if type =='quotation':
            print(INFO, type)

            queryset = Invoices.objects.filter(Q(quotation=1)|Q(quotation=-1)).order_by('-id')
            print(queryset)
            queryset = Invoices.objects.filter(quotation__in=[1,-1]).order_by('-id')

            # print(queryset.query)
            return queryset

        elif type =='sales_order':
            queryset = Invoices.objects.all().filter(Q(sales_order=1)|Q(sales_order=-1)).order_by('-id')
            # print(queryset.query)
            print(INFO,type)
            return queryset

        elif type =='invoice':
            queryset = Invoices.objects.filter(Q(invoice=1)|Q(invoice=-1)).order_by('-id')
            # print(queryset.query)
            print(INFO,type)
            return queryset

        else:
        # queryset = Invoices.objects.prefetch_related('items').all().order_by('-id')
        # queryset = Invoices.objects.raw('SELECT id, customer FROM airapanel_invoices ')
            print(queryset.query)
            return queryset
    def post(self,reqeust):
        return Response("Not working")


        cst_id = self.request.POST.get('cst_id','')
        due_date = self.request.POST.get('due_date', '')
        cmp_id = self.request.POST.get('cmp_id','')
        total_amount = self.request.POST.get('total_amount')
        paid_amount = float(self.request.POST.get('paid_amount','0'))

        items = self.request.POST.get('items','')
        items = json.loads(items)

        action = self.request.POST.get('action')

        bill_type = self.request.POST.get('bill_type','')

        if action == "" or not action:
            return Response(
                {
                    STATUS: False,
                    MESSAGE:"Required 'action' ",
                    CODE:"d1e23rf1",
                }
            )

        if bill_type == "" or not bill_type:
            return Response(
                {
                    STATUS: False,
                    MESSAGE:"Required 'bill_type' ",
                    CODE:"d1e23rfas1",
                }
            )
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
        inv_obj.total_amount = total_amount
        inv_obj.paid_amount = paid_amount
        inv_obj.customer = Customers.objects.filter(id=cst_id).first()
        inv_obj.company = Companies.objects.filter(id=cmp_id).first()
        # cust_name = Customers.objects.filter(id=cst_id).first().name
        # cmp_name = Companies.objects.filter(id=cst_id).first().name
        # inv_obj.customer_name = cust_name
        # inv_obj.company_name = cmp_name


        type_obj = Type_of_voucher()

        if action == "quotation_save":
            msg = " Action "+ action

            type_obj.modified = datetime. now()
            unique_id = 'asd'
            type = bill_type
            status = "quotation"

            # inv_obj.quotation = 1
            # # inv_obj.sales_order = 0
            # # inv_obj.invoice = 0
            #
            # inv_obj.quotation_status = "quotation"
            # # inv_obj.sales_order_status = ''
            # # inv_obj.invoice_status = ''

        elif action == "quotation_send_email":
            msg = " Action "+ action
            # sendemailfunction()
            type_obj.modified = datetime.now()
            unique_id = 'asd'
            type = bill_type
            status = "quotation_send"

            # inv_obj.quotation = 1
            # # inv_obj.sales_order = 0
            # # inv_obj.invoice = 0
            #
            # inv_obj.quotation_status = "quotation_send"
            # # inv_obj.sales_order_status = ''
            # # inv_obj.invoice_status = ''

        elif action == "quotation_confirm":
            msg = " Action " + action
            type_obj.modified = datetime.now()
            unique_id = 'asd'
            type = bill_type
            status = "quotation_send"


            inv_obj.quotation = 1
            inv_obj.sales_order = 1
            # inv_obj.invoice = 1

            inv_obj.quotation_status = "sales_order"
            inv_obj.sales_order_status = "to_invoice"
            inv_obj.invoice_status = ''

        elif action == "quotation_cancel":
            msg = " Action "+ action

            inv_obj.quotation = -1
            inv_obj.sales_order = 0
            inv_obj.invoice = 0

            inv_obj.quotation_status = "Canceled"
            # inv_obj.sales_order_status = ''
            # inv_obj.invoice_status = ''

        elif action == "invoice_save":
            msg = " Action "+ action

            # inv_obj.quotation = 0
            # inv_obj.sales_order = 0
            inv_obj.invoice = 1

            inv_obj.quotation_status = "draft"
            # inv_obj.sales_order_status = ''
            # inv_obj.invoice_status = ''

        elif action == "invoice_post":
            msg = " Action "+ action

            # inv_obj.quotation = 1
            # inv_obj.sales_order = 0
            inv_obj.invoice = 1

            # inv_obj.quotation_status = "quotation"
            # inv_obj.sales_order_status = ''
            inv_obj.invoice_status = "posted"

        else :
            msg = " Action " + action
            return Response(
                {
                    STATUS:False,
                    MESSAGE:"undefined action name: '"+action+"'",
                    CODE:"1235dd2",
                    ACTION: msg,

                }
            )



        # return Response(
        #     {
        #         STATUS: False,
        #         CODE: "1235d12e",
        #         ACTION: msg,
        #
        #     }
        # )
        try:
            inv_obj.save()
            print(INFO,"invoice id ",inv_obj.id)
            instance = []
            for item in items:
                # print(Products.objects.filter(id=item['id']).first())
                print(item['id'], "rs ", item['price'])
                instance.append(
                    ItemsInvoice(
                        invoiceId=inv_obj.id,

                        product_Id=Products.objects.filter(id=item['id']).first(),
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
            print("Excepction :"+str(e)+ " Line no :"+ str(format(sys.exc_info()[-1].tb_lineno)))
            inv_obj.delete()
            return Response(
                {
                    STATUS:False,
                    "Excepction":str(e),
                    MESSAGE:"requred cst_id, due_date, cmp_id, status, total_amount, [paid_amount] ",
                }
            )
    def put(self,reqeust):
        return Response("not owrking")
        invoice_id = self.request.POST.get('id')

        cst_id = self.request.POST.get('cst_id', '')
        due_date = self.request.POST.get('due_date', '')
        cmp_id = self.request.POST.get('cmp_id', '')
        total_amount = self.request.POST.get('total_amount')
        paid_amount = float(self.request.POST.get('paid_amount', '0'))

        items = self.request.POST.get('items', '')
        items = json.loads(items)

        action = self.request.POST.get('action')

        if invoice_id == "" or not invoice_id:
            return Response(
                {
                    STATUS: False,
                    MESSAGE: "Required 'invoice_id' ",
                    CODE: "d1d13d1",
                }
            )

        if action == "" or not action:
            return Response(
                {
                    STATUS: False,
                    MESSAGE: "Required 'action' ",
                    CODE: "d1e23rf1",
                }
            )

        # the result is a Python dictionary:
        # ItemsInvoice.objects.raw(
        #     "INSERT INTO airapanel_itemsinvoice (invoiceId, item_price, tax) "
        #     # "VALUES ("'inv_obj.id'",  )"
        #     "VALUES ("'7'","'32'"," '23' ")"
        # )
        # for x in Invoices.objects.raw("SELECT * FROM airapanel_invoices"):
        #     print(x.id)

        inv_obj = Invoices.objects.filter(id=invoice_id)
        if not inv_obj.exists():
            return Response(
                {
                    STATUS:False,
                    MESSAGE:"No such data",
                    CODE:"d1d14t3qf",
                }
            )

        inv_obj.due_date = due_date
        inv_obj.total_amount = total_amount
        inv_obj.paid_amount = paid_amount
        inv_obj.customer = Customers.objects.filter(id=cst_id).first()
        inv_obj.company = Companies.objects.filter(id=cmp_id).first()

        # inv_obj.customer = cmp_id
        # inv_obj.company = cst_id
        # cust_name = Customers.objects.filter(id=cst_id).first().name
        # cmp_name = Companies.objects.filter(id=cst_id).first().name
        # inv_obj.customer_name = cust_name
        # inv_obj.company_name = cmp_name


        try:
            inv_obj.save()
            print(INFO, "invoice id ", inv_obj.id)
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

            for x in ItemsInvoice.objects.filter(invoiceId=inv_obj.id):
                inv_obj.items.add(x)

            # obj = ItemsInvoice(obj)
            # obj.save()
            # for x in

            # ItemsInvoice.objects.bulk_create()

            # inv_obj.delete()
            if float(paid_amount) > 0.0:
                'if any advance amount paid, it will be recorded in payement history'
                print("Advance paid")
                description = 'advance'
                ph_obj = PayemetHistory.objects.filter()
                ph_obj.invoice_id = inv_obj.id
                ph_obj.date_of_payement = inv_obj.created
                ph_obj.amount = paid_amount
                ph_obj.description = description
                ph_obj.save()
                inv_obj.payement_history.add(ph_obj)
            return Response(
                {
                    STATUS: True,
                    MESSAGE: "New invoice added",
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
                    STATUS: False,
                    "Excepction": str(e),
                    MESSAGE: "requred cst_id, due_date, cmp_id, status, total_amount, [paid_amount] ",
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
        return Response("Not workg")
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







#
# class InvoiceAction(ListAPIView):
#     serializer_class = InvoiceSerializers
#
#
#     def get(self,request):
#         return Response(
#             {
#                 STATUS:True,
#                 MESSAGE:"invoice actions [quotation_save, quotation_send_email, quotation_confirm, quotation_cancel, set_to_quotation, invoice_save, invoice_post, invoice_cancel]",
#             }
#         )
#     def put(self,request):
#         action = self.request.POST.get('action','')
#         id = self.request.POST.get('id')  #invoice id
#
#         if action == '' or not action:
#             return Response(
#                 {
#                     STATUS:False,
#                     MESSAGE:"required action",
#                     CODE:"1232f3",
#                 }
#             )
#
#         if id == '' or not id:
#             return Response(
#                 {
#                     STATUS:False,
#                     MESSAGE:"required id",
#                     CODE:"1qw2f33",
#                 }
#             )
#
#         inv_obj = Invoices.objects.filter(id=id)
#         if not inv_obj.exists():
#             return Response(
#                 {
#                     STATUS:False,
#                     MESSAGE:"No such invoice data with id ",
#                     CODE:"jn0231",
#                 }
#             )
#
#         else:
#             inv_obj = inv_obj.first()
#
#         if action == "quotation_save":
#             msg = " Action "+ action
#             inv_obj.quotation = 1
#             # inv_obj.sales_order = 0
#             # inv_obj.invoice = 0
#
#             inv_obj.quotation_status = "quotation"
#             # inv_obj.sales_order_status = ''
#             # inv_obj.invoice_status = ''
#
#         elif action == "quotation_send_email":
#             msg = " Action "+ action
#
#             inv_obj.quotation = 1
#             # inv_obj.sales_order = 0
#             # inv_obj.invoice = 0
#
#             inv_obj.quotation_status = "quotation"
#             send_invoice(id)
#
#             # inv_obj.sales_order_status = ''
#             # inv_obj.invoice_status = ''
#
#         elif action == "quotation_confirm":
#             msg = " Action " + action
#
#             # inv_obj.quotation = 1
#             inv_obj.sales_order = 1
#             # inv_obj.invoice = 1
#
#             inv_obj.quotation_status = "sales_order"
#             inv_obj.sales_order_status = "to_invoice"
#             inv_obj.invoice_status = ''
#
#         elif action == "quotation_cancel":
#             msg = " Action "+ action
#
#             inv_obj.quotation = -1
#             inv_obj.sales_order = 0
#             inv_obj.invoice = 0
#
#             inv_obj.quotation_status = "Canceled"
#             # inv_obj.sales_order_status = ''
#             # inv_obj.invoice_status = ''
#
#         elif action == "set_to_quotation":
#             msg = " Action "+ action
#
#             inv_obj.quotation = 1
#             # inv_obj.sales_order = 0
#             # inv_obj.invoice = 0
#
#             inv_obj.quotation_status = "quotation"
#             # inv_obj.sales_order_status = ''
#             # inv_obj.invoice_status = ''
#
#         elif action == "invoice_save":
#             msg = " Action "+ action
#
#             # inv_obj.quotation = 0
#             # inv_obj.sales_order = 0
#             inv_obj.invoice = 1
#
#             # inv_obj.quotation_status = "quotation"
#             # inv_obj.sales_order_status = ''
#             '''if amount fully paid then status to paid else not paid'''
#             inv_obj.invoice_status = 'draft'
#
#         # elif action == "register_payement":
#         #     msg = " Action "+ action
#         #
#         #     # inv_obj.quotation = 0
#         #     # inv_obj.sales_order = 0
#         #     # inv_obj.invoice = 1
#         #
#         #     # inv_obj.quotation_status = "quotation"
#         #     # inv_obj.sales_order_status = ''
#         #     '''if amount fully paid then status to paid else not paid'''
#         #     inv_obj.invoice_status = 'paid/not_paid'
#
#         elif action == "invoice_post":
#             msg = " Action "+ action
#
#             # inv_obj.quotation = 0
#             # inv_obj.sales_order = 0
#             inv_obj.invoice = 1
#
#             # inv_obj.quotation_status = "quotation"
#             # inv_obj.sales_order_status = ''
#             '''if amount fully paid then status to paid else not paid'''
#             inv_obj.invoice_status = 'posted'
#
#         elif action == "invoice_cancel":
#             msg = " Action "+ action
#
#             # inv_obj.quotation = 0
#             # inv_obj.sales_order = 0
#             inv_obj.invoice = -1
#
#             # inv_obj.quotation_status = "quotation"
#             # inv_obj.sales_order_status = ''
#             '''if amount fully paid then status to paid else not paid'''
#             inv_obj.invoice_status = 'cancelled'
#
#         # elif action == "":
#         #     msg = " Action "+ action
#         # elif action == "":
#         #     msg = " Action "+ action
#
#         else :
#             msg = " Action " + action
#             return Response(
#                 {
#                     STATUS:False,
#                     MESSAGE:"undefined action name: '"+action+"'",
#                     CODE:"1235dd2",
#                     ACTION: msg,
#
#                 }
#             )
#
#         try:
#             inv_obj.save()
#
#             return Response(
#                 {
#                     STATUS:True,
#                     MESSAGE:action+ " completed",
#                 }
#             )
#         except Exception as e:
#             return Response(
#                 {
#                     STATUS: True,
#                     MESSAGE: action + " not completed",
#                     CODE:"674722f",
#
#                 }
#             )
#


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
            amount = float(self.request.POST.get('amount',0.0))
            date_of_payement = self.request.POST.get('date_of_payement','')

            if not amount or amount ==0:
                return Response(
                    {
                        STATUS:False,
                        MESSAGE:"required amount",
                    }
                )

            if not date_of_payement or date_of_payement ==0:
                return Response(
                    {
                        STATUS:False,
                        MESSAGE:"date_of_payement",
                    }
                )

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
                    pending_amount = float(total_amount) - float(i_obj.paid_amount) - float(amount)

                    ph_obj = PayemetHistory()
                    ph_obj.invoice_id = id
                    ph_obj.date_of_payement = date_of_payement
                    ph_obj.amount = amount



                    if pending_amount <= 0:
                        i_obj.status = "paid"
                        msg = "thank you , you closed the invoice amount"
                    else:
                        i_obj.status = "paritally_paid"
                        msg = "thank you , we expecting your remaning due soon"
                    i_obj.paid_amount = float(i_obj.paid_amount) + float(amount)

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


class Test(ListAPIView):
    def get(self,request):
        obj1 = Table1(name="jasir1")
        obj2 = Table2(name="jasir2")
        # Table2().

        obj = obj2+obj1
        print(obj)
        return Response(True)

def send_invoice(id):
    return "Not working"
    invoice = Invoices.objects.filter(id=id)
    items = "<tr class='heading'> <td> Item </td> <td> Price </td>  </tr>"
    total = 0.0
    invoice_number = 0000
    created = 0000
    due_date = 000
    address_from = {
        "from": "Jasir",
        "company": "Codedady",
        "email": "jasirmj@gmail.com",
    }
    address_to = {
        "to": "customer1",
        "company": "fb",
    }
    for x in invoice:
        invoice_number = x.id
        created = x.created.strftime('%d %B %Y')
        due_date = x.due_date.strftime('%d %B %Y')
        address_to['to'] = x.customer.name
        address_to['company'] = x.company.name

        iteminv_obj = Sales.objects.filter(invoiceId=x.id)
        # print("iteminv_obj :", iteminv_obj)
        for y in iteminv_obj:
            total = total + float(y.item_price)
            items = items + '<tr class="item"><td>' + y.product_Id.name + '</td><td>' + str(y.item_price) + '</td></tr>'


        payements = '<tr class="heading"><td>payement date</td><td>amount</td></tr>'
        payement_obj = PayemetHistory.objects.filter(invoice_id=id)
        # print(payement_obj)
        for payement in payement_obj:
            payements = payements + '<tr><td>'+payement.date_of_payement.strftime("%d-%m-%y")+'</td><td>'+str(payement.amount)+'</td></tr>'
            # print(payements)

            # print("item price :", y.item_price)
            # print("product_Id :", y.product_Id)
            # print("product.name :", y.product_Id.name)



    mail = 'jasirmj@gmail.com'

    # inv_obj = Invoices.objects.filter(id=id).first()
    # print('inv obj ',inv_obj)
    # print('customer_name :',inv_obj.customer_name)
    # print('company_name :',inv_obj.company_name)
    # print('due date :',inv_obj.due_date)
    # print('items :',inv_obj.items)



    # items_list = ['computer', 'software service', 'mouse', 'webdevelopement', 'book', 'marker', 'door', 'charger',
    #               'table', 'ac', 'tv', 'fan', 'headset', 'pen', 'pencil', 'waterbottle', 'iphone', 'redmi', 'samsung',
    #               'nexus', 'bag', 'chair', ]
    # items_price = [20000, 35000, 34, 45, 56, 56, 877, 45, 3443, 55, 44, 77, 222, 445, 767, 1234, 122, 111, 455, 444,
    #                555, 56, 5788, 123, 43, 534, 234, 234, 234, 23, 423, 4, 234, 234, 23, 534, 2, 5234, 52, 634, 1123,
    #                234, 32423, 12543, 123, 123]

    #
    # items = "<tr class='heading'> <td> Item </td> <td> Price </td>  </tr>"
    #
    # for x in range(1, 10):
    #     total = total + items_price[x]
    #     items = items + '<tr class="item"><td>' + items_list[x] + '</td><td>' + str(items_price[x]) + '</td></tr>'
    template = '''
    <!doctype html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>invoice</title>
        <style>
        .invoice-box {
            max-width: 800px;
            margin: auto;
            padding: 30px;
            border: 1px solid #eee;
            box-shadow: 0 0 10px rgba(0, 0, 0, .15);
            font-size: 16px;
            line-height: 24px;
            font-family: 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;
            color: #555;
        }
    
        .invoice-box table {
            width: 100%;
            line-height: inherit;
            text-align: left;
        }
    
        .invoice-box table td {
            padding: 5px;
            vertical-align: top;
        }
    
        .invoice-box table tr td:nth-child(2) {
            text-align: right;
        }
    
        .invoice-box table tr.top table td {
            padding-bottom: 20px;
        }
    
        .invoice-box table tr.top table td.title {
            font-size: 45px;
            line-height: 45px;
            color: #333;
        }
    
        .invoice-box table tr.information table td {
            padding-bottom: 40px;
        }
    
        .invoice-box table tr.heading td {
            background: #eee;
            border-bottom: 1px solid #ddd;
            font-weight: bold;
        }
    
        .invoice-box table tr.details td {
            padding-bottom: 20px;
        }
    
        .invoice-box table tr.item td{
            border-bottom: 1px solid #eee;
        }
    
        .invoice-box table tr.item.last td {
            border-bottom: none;
        }
    
        .invoice-box table tr.total td:nth-child(2) {
            border-top: 2px solid #eee;
            font-weight: bold;
        }
    
        @media only screen and (max-width: 600px) {
            .invoice-box table tr.top table td {
                width: 100%;
                display: block;
                text-align: center;
            }
    
            .invoice-box table tr.information table td {
                width: 100%;
                display: block;
                text-align: center;
            }
        }
    
        /** RTL **/
        .rtl {
            direction: rtl;
            font-family: Tahoma, 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;
        }
    
        .rtl table {
            text-align: right;
        }
    
        .rtl table tr td:nth-child(2) {
            text-align: left;
        }
        </style>
    </head>
    
    <body>
        <div class="invoice-box">
            <table cellpadding="0" cellspacing="0">
                <tr class="top">
                    <td colspan="2">
                        <table>
                            <tr>
                                <td class="title">
                                    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTK4yHZUTNYyi-TEiXhxOy6TVF8CwMCvX9IiGp0Ta1aGyhuboYe&s" style="width:100px; max-width:300px;">
                                </td>
    
                                <td>
                                    Invoice #: '''+str(invoice_number)+'''<br>
                                    Created: '''+str(created)+'''<br>
                                    Due: '''+str(due_date)+'''
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
                <tr class="information">
                    <td colspan="2">
                        <table>
                            <tr>
                                <td>
                                    '''+str(address_from['from'])+'''<br>
                                    '''+str(address_from['company'])+''' <br>
                                    '''+str(address_from['email'])+''' <br>
                                </td>
    
                                <td>
                                    '''+str(address_to['to'])+'''.<br>
                                    '''+str(address_to['company'])+'''<br>
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
    
                
                ''' + items + '''
    
    
    
                <tr class="total">
                    <td></td>
    
                    <td>
                       Total: &#x20b9;''' + str(total) + '''
                    </td>
                </tr>
                <tr class="details">
                    <td>
                    </td>
                    <td>
                        <table>                          
                            '''+payements+'''                         
                        </table>
                    </td>
                </tr>
            </table>
        </div>
    </body>
    </html>
'''

    # message = Mail(
    #     from_email='airatest.admin@no-replay.com',
    #     to_emails= 'jasirmj@gmail.com' ,
    #     subject="Codedady Invoice1",
    #     html_content=template)

    pdfname = "invoicetemp.pdf"
    

    path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
    # pdfkit.from_url("http://google.com", "out.pdf", configuration=config)
    pdfkit.from_string(template, pdfname, configuration=config)


    # cwd = os.getcwd()  # Get the current working directory (cwd)
    # files = os.listdir(cwd)  # Get all the files in that directory
    # print("Files in %r: %s" % (cwd, files))

    file_path = pdfname
    with open(file_path, 'rb') as f:
        data = f.read()
        f.close()
    encoded = base64.b64encode(data).decode()



    SUBJECT = "Codedady Invoice"
    url = "https://api.sendgrid.com/v3/mail/send"
    data = {
        "personalizations": [
            {
                "to": [
                    {
                        "email": mail,
                        # "email": 'anas.melepeediakkal@gmail.com',
                    }
                ]
            }
        ],
        "from": {
            "email": "aira.admin@no-replay.com"
        },
        "subject": SUBJECT,

        "attachments": [
            {
                "content": encoded,
                "content_id": "ii_139db99fdb5c3704",
                "disposition": "inline",
                "filename": pdfname,
                "name": "jasir1",
                "type": "pdf"
            }
        ],

        "content": [
            {
                "type": "text/html",
                "value": template

            }
        ]
    }
    headers = {
        'Content-type': 'application/json',
        # 'Accept': 'text/plain',
        # 'Authorization': 'Bearer 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',
        'Authorization': 'Bearer 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',
    }

    r = requests.post(url, data=json.dumps(data), headers=headers)
    print(r)


