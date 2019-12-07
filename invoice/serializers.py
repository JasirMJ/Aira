from rest_framework import serializers, exceptions
from AiraPanel.models import *
from AiraPanel.serializers import *

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = '__all__'

class PayemetHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PayemetHistory
        fields = '__all__'

class CustomerSerializersInvoice(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = ['id','name','aira_code','address','email','mobile','phone']
# class DashBoardSerializer(serializers.ModelSerializer):
#     leave = serializers.SerializerMethodField()
#     notification = serializers.SerializerMethodField()
#     class Meta:
#         model = SNITUsers
#         fields = '__all__'
#     def get_leave(self, obj) :
#         print("Current user :",obj.userid.id)
#         leave_instance = Leave.objects.filter(userid_id=obj.userid.id).order_by('-id').exclude(Q(status="approved" ) or Q(status="rejected") )
#         if leave_instance.exists() :
#             response = LeaveSerializer(leave_instance,many=True)
#             return response.data
#         else :
#             print("0 Leave ")
#             return 0

class SalesSerializers(serializers.ModelSerializer):
    items = Items_relationSerializers(many=True)
    customer = CustomerSerializersInvoice()
    company = CompanySerializers()
    history = HistorySerializer(many = True)

    class Meta:
        model = Sales
        fields = '__all__'

# class InvoiceSerializers(serializers.ModelSerializer):


class InvoiceSerializers(serializers.ModelSerializer):
    # payement_details = serializers.SerializerMethodField()
    # customer_details = serializers.SerializerMethodField()
    # company_details = serializers.SerializerMethodField()
    # items_details = serializers.SerializerMethodField()

    items = Items_relationSerializers(many=True)
    payement_history = PayemetHistorySerializer(many=True)
    customer = CustomerSerializersInvoice()
    company = CompanySerializers()
    history = HistorySerializer(many = True)


    # customer = CustomerSerializers(many=True)

    class Meta:
        model = Invoices
        fields = '__all__'

    # def get_company_details(self, obj):
    #     # print("obj ",obj)
    #     # cmp_id = Invoices.objects.filter(id=obj.id).first().customer.all().first().id
    #
    #     details = Companies.objects.filter(id=obj.company)
    #     # print(details)
    #     print("invopice ",Companies.objects.filter(id=obj.company).first())
    #     if details.exists() :
    #         details = Companies.objects.filter(id=obj.company).order_by('id')
    #         response = CompanySerializers(details,many=True)
    #         return response.data
    #     else :
    #         print("0 companies")
    #         return 0
    #
    # def get_customer_details(self, obj):
    #     print("obj ",obj)
    #     # details = Customers.objects.filter(id=obj.id)
    #     # cust_id = Invoices.objects.filter(id=obj.id).first().customer.all().first().id
    #
    #     details = Customers.objects.filter(id= obj.customer)
    #     # print(details)
    #     if details.exists() :
    #         # details = Customers.objects.filter(id=obj.id).order_by('id')
    #         details = Customers.objects.filter(id= obj.customer).order_by('id')
    #         response = CustomerSerializers(details,many=True)
    #         return response.data
    #     else :
    #         print("0 customers ")
    #         return 0
    #
    # def get_items_details(self, obj):
    #     # print("obj ",obj)
    #     details = ItemsInvoice.objects.filter(invoiceId=obj.id)
    #     # print(payement_details)
    #     if details.exists() :
    #         details = ItemsInvoice.objects.filter(invoiceId=obj.id).order_by('id')
    #         response = ItemsInvoiceSerializers(details,many=True)
    #         return response.data
    #     else :
    #         print("0 items")
    #         return 0
    #
    # def get_payement_details(self, obj):
    #     # print("obj ",obj)
    #     payement_details = PayemetHistory.objects.filter(invoice_id=obj.id)
    #     # print(payement_details)
    #     if payement_details.exists() :
    #         payement_details = PayemetHistory.objects.filter(invoice_id=obj.id).order_by('id')
    #         response = PayemetHistorySerializer(payement_details,many=True)
    #         return response.data
    #     else :
    #         print("0 payement history ")
    #         return 0

