import sys

from django.db import transaction
from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.utils import json
from AiraPanel.models import *
from AiraPanel.global_variables import *
# Create your views here.
from rest_framework.generics import ListAPIView

from purchase.serializers import *


class ContractView(ListAPIView):
    serializer_class = ContractViewSerializer
    def get_queryset(self):
        queryset = PurchaseContracts.objects.all().order_by('-id')
        # queryset.delete()
        return queryset

    def post(self,request):
        try:
            data = []
            items = self.request.POST.get('items', '')
            vendors = self.request.POST.get('vendors', '')
            end_date = self.request.POST.get('end_date', '')

            items = json.loads(items)
            vendors = json.loads(vendors)

            data.append(
                {
                    "vendors":vendors,
                    "items":items,
                    "contract_up_to":str(end_date),
                }
            )

            instance = []

            pc_obj = PurchaseContracts()
            pc_obj.contract_id = "purchase_contract_id"
            pc_obj.end_date = end_date
            pc_obj.save()
            print("Purchase contract saved")

            # pc_id = PurchaseContracts.objects.last().id
            print("last pc id ",pc_obj.id)
            for item in items:
                print(item," added to list")

                instance.append(
                    Purchase_Items_relation(
                        contract_id = pc_obj.id + 1 ,
                        purchase_id = 'Purchase_id_here',
                        product_Id = Products.objects.filter(id=item['id']).first(),
                    )
                )

            with transaction.atomic():

                Purchase_Items_relation.objects.bulk_create(instance)
                print("items relation created")

                for vendor in vendors:
                    obj = Customers.objects.filter(id=vendor['id']).first()
                    pc_obj.vendors.add(obj)
                    print("vendor added ",obj)

                for x in Purchase_Items_relation.objects.filter(contract_id=pc_obj.id):
                    obj = Purchase_Items_relation.objects.filter(id = x.id).first()
                    pc_obj.items.add(obj)

            print("Purchase contract saved")

            return Response(
                {
                    STATUS : True,
                    MESSAGE : "Contract created",
                    "Data" : data,
                }
            )

        except Exception as e:
            print("Exception : ",str(e))
            return Response(
                {
                    STATUS: False,
                    MESSAGE: "Contract not created",
                    "Exception": str(e),
                    "Line no": printLineNo(),
                }
            )

class PurchaseOrderView(ListAPIView):
    serializer_class = PurchaseOrderSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        '''
        :return:
        '''
        queryset = PurchaseOrder.objects.all().order_by('-id')
        return queryset

    def post(self,request):
        username = self.request.user.username
        userid = self.request.user.id



        whoami(request)

        aira_obj = AiraAuthentication.objects.filter(user_id_id=self.request.user.id).first()
        print("aira :", aira_obj)

        comp_obj = aira_obj.company_id
        print("company :", comp_obj)


        '''
        :param request:

        :return:

        '''

        try:

            #To store all the params and return when sucess
            data = []

            #reading data
            items = self.request.POST.get('items', '')
            vendors = self.request.POST.get('vendors', '')
            contract_referance = self.request.POST.get('contract_referance', '')
            vendor_referance = self.request.POST.get('vendor_referance', '')

            status = self.request.POST.get('status', '')
            billing_status = self.request.POST.get('billing_status', 'nothing to bill')
            purchase_by = self.request.POST.get('purchase_by', '')

            total_amount = self.request.POST.get('total_amount')
            paid_amount = float(self.request.POST.get('paid_amount', '0'))

            #fetching item str to json convesion
            items = json.loads(items)
            vendors = json.loads(vendors)

            if aira_obj.type == "company":
                branch_id = self.request.POST.get("branch_id", "")
                if branch_id == "" or not branch_id:
                    return Response(
                        {
                            STATUS: False,
                            MESSAGE: "Required branch_id"
                        }
                    )

                branch_obj = comp_obj.branch_id.filter(id=branch_id)
                print("branch obj ", branch_obj)
                if branch_obj.exists():
                    # obj = Branch.objects.filter(id=branch_id)
                    # comp_obj.branch_id.filter(product_branch=obj)
                    # print(comp_obj.filter(branch_id=obj))
                    # if obj.exists():
                    branch_obj = branch_obj.first()
                    print(branch_obj)
                else:
                    return Response(
                        {
                            STATUS: False,
                            MESSAGE: "Please provide a branch id under your company"
                        }
                    )
            else:
                branch_obj = aira_obj.branch_id
                print("branch :", branch_obj)

            print("got branch b ", branch_obj)
            # return Response(True)

            # action = self.request.POST.get('action', '')
            # if isnull(action):
            #     print("action is null")
            # else:
            #     print("action value is ",action)

            #adding data to list
            data.append(
                {
                    "vendors": vendors,
                    "items": items,
                    "status": status,
                    "billing_status": billing_status,
                    "purchase_by": purchase_by,
                    "contract_referance": contract_referance,
                    "vendor_referance": vendor_referance,
                    "total_amount":total_amount,
                    "paid_amount":paid_amount,
                }
            )


            #instance for bulk insert for PurchaseOrder
            instance = []


            fully_billed = "fully billed"

            pc_obj = PurchaseOrder()
            pc_obj.contract_referance = contract_referance
            pc_obj.status = status
            pc_obj.billing_status = billing_status
            pc_obj.vendor_referance = vendor_referance
            pc_obj.paid_amount = paid_amount
            pc_obj.total_amount = total_amount





            # return Response(True)

            with transaction.atomic():
                pc_obj.save()
                print("Purchase order saved")

                # pc_id = PurchaseContracts.objects.last().id
                print("last pc id ", pc_obj.id)

                # instance for bulk insert for Inventory
                inventory_instance = []

                # to save item id for iteration purpose , used to specify in ORM
                item_id = []

                # to save items, and take data from it during iteration
                items_list = []

                for item in items:
                    print(item, " added to list")
                    instance.append(
                        Purchase_Items_relation(
                            contract_id=pc_obj.id + 1,
                            purchase_id='Purchase_id_here',
                            product_Id=Products.objects.filter(id=item['id']).first(),
                            item_price=float(item['price']),
                            tax=item['tax'],
                        )
                    )

                    inventory_instance.append(
                        Inventory(
                            itemid=Products.objects.filter(id=item['id']).first(),
                            item_in=item['qty'],
                            type="purchase",
                            unit_price=float(item['price']) * float(item['qty']),
                            # unit_price= "",
                            barcodeid="TEST_CODE",
                            branch=branch_obj,
                        )
                    )

                    item_id.append(item['id'])
                    items_list.append(
                        {
                            'id': item['id'],
                            'qty': item['qty'],
                        }
                    )
                print("Item list ", items_list)



                pdt_objs = Products.objects.filter(id__in=item_id)
                branch_pdt_objs = pdt_objs.filter(branch__id=branch_obj.id)


                flag = 0
                unavailable = []
                for x in pdt_objs:
                    print("pdt : ",x.id)

                    if x in branch_pdt_objs:
                        print(x.id," Item found")
                    else:
                        print(x.id," Item not found")
                        unavailable.append(
                            {
                                "id":x.id,
                                "name":x.name
                            }
                        )
                        flag = 1

                if flag == 1:
                    return Response(
                        {
                            STATUS:False,
                            MESSAGE:"please add the following products first",
                            "cant_find":unavailable,
                        }
                    )

                # print("pdt_objs1", pdt_objs)
                # pdt_objs = pdt_objs.filter(branch__id = branch_obj.id)
                # print("pdt_objs2", branch_pdt_objs)

                # return Response(True)
                x = 0
                for pdt_obj in pdt_objs:
                    print(pdt_obj.name, " old stock " + str(pdt_obj.stock))
                    pdt_obj.stock += float(items_list[x]['qty'])
                    pdt_obj.branch = branch_obj
                    print(pdt_obj.name, "new stock " + str(pdt_obj.stock))
                    print(str(items_list[x]['qty']) + ' was added')
                    x += 1


                # Save all objects in 1 query
                Products.objects.bulk_update(pdt_objs, ['stock'])  # updating stok in Product

                # print("changed : ",o)
                print('data ', items_list[0]['qty'])
                Purchase_Items_relation.objects.bulk_create(instance)
                print("items relation created")
                Inventory.objects.bulk_create(inventory_instance)
                print("inventory created")




                for vendor in vendors:
                    obj = Customers.objects.filter(id=vendor['id']).first()
                    pc_obj.vendors.add(obj)
                    print("vendor added ", obj)

                for x in Purchase_Items_relation.objects.filter(contract_id=pc_obj.id):
                    obj = Purchase_Items_relation.objects.filter(id=x.id).first()
                    pc_obj.items.add(obj)

                print("Purchase order saved")

                if float(paid_amount) > 0.0 :
                    'if any advance amount paid, it will be recorded in payement history'
                    print("Advance paid")
                    description = 'advance'
                    ph_obj = PurchasePayemetHistory()
                    ph_obj.purchase_id = pc_obj.id
                    ph_obj.date_of_payement = pc_obj.created
                    ph_obj.amount = paid_amount
                    ph_obj.description = description
                    ph_obj.save()
                    pc_obj.payement_history.add(ph_obj)


            return Response(
                {
                    STATUS: True,
                    MESSAGE: "Purchase order created",
                    "Data": data,
                }
            )

        except Exception as e:
            print("Exception : ", str(e))
            return Response(
                {
                    STATUS: False,
                    MESSAGE: "Purchase order not created",
                    "Exception": str(e),
                    "Line no": printLineNo(),
                }
            )

# class CreateBill(ListAPIView):
#
#     def post(self,request):
#
#         data = []
#
#         items = self.request.POST.get('items', '')
#         vendors = self.request.POST.get('vendors', '')
#         contract_referance = self.request.POST.get('contract_referance', '')
#         vendor_referance = self.request.POST.get('vendor_referance', '')
#
#         status = self.request.POST.get('status', '')
#         billing_status = self.request.POST.get('billing_status', 'nothing to bill')
#         purchase_by = self.request.POST.get('purchase_by', '')
#
#         items = json.loads(items)
#         vendors = json.loads(vendors)
#
#         po_id = self.request.POST.get('po_id','')
#
#         if po_id == "":
#             '''Create new bill'''
#             print('Create new bill')
#         else:
#             '''Create bill on existing order'''
#             print('Create bill on existing order')
#
#
#         data.append(
#             {
#                 "vendors": vendors,
#                 "items": items,
#                 "status": status,
#                 "billing_status": billing_status,
#                 "purchase_by": purchase_by,
#                 "contract_referance": contract_referance,
#                 "vendor_referance": vendor_referance,
#             }
#         )
#
#         return Response(
#             {
#                 STATUS:True,
#                 MESSAGE:"Sucess",
#             }
#         )

class InventoryView(ListAPIView):
    serializer_class = InventoryViewSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        username = self.request.user.username
        userid = self.request.user.id

        aira_obj = AiraAuthentication.objects.filter(user_id_id=self.request.user.id).first()
        print(aira_obj)

        comp_obj = aira_obj.company_id

        branch_obj = aira_obj.branch_id

        if aira_obj.type == "company":
            print("Company name :", comp_obj.name)

            print("Got company request ", username)
            queryset = Inventory.objects.filter(company=comp_obj)
        elif aira_obj.type == "branch":
            print("Company name :", comp_obj.name)
            print("Branch name :", branch_obj.name)

            print("Got branch request ", username)
            queryset = Inventory.objects.filter(branch=branch_obj)
        elif aira_obj.type == "counter":
            print("Company name :", comp_obj.name)
            print("Branch name :", branch_obj.name)

            print("Got counter request ", username)
            queryset = Inventory.objects.filter(branch=aira_obj.branch_id)
        else:
            queryset = Inventory.objects.none()

        # qs = Inventory.objects.all().order_by('-id')
        return queryset

class PurchasePayement(ListAPIView):

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

            p_obj = PurchaseOrder.objects.filter(id=id)
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

            if p_obj.exists():
                msg = "invoice found"

                p_obj = p_obj.first()
                total_amount = p_obj.total_amount
                if p_obj.status == "paid":
                    return Response(
                        {
                            STATUS:True,
                            MESSAGE:"balance_closed",
                        }
                    )
                if amount:
                    print('amount')
                    pending_amount = float(total_amount) - float(p_obj.paid_amount) - float(amount)

                    ph_obj = PurchasePayemetHistory()
                    ph_obj.purchase_id = id
                    ph_obj.date_of_payement = date_of_payement
                    ph_obj.amount = amount



                    if pending_amount <= 0:
                        p_obj.status = "paid"
                        msg = "thank you , you closed the invoice amount"
                    else:
                        p_obj.status = "paritally_paid"
                        msg = "thank you , we expecting your remaning due soon"
                    p_obj.paid_amount = float(p_obj.paid_amount) + float(amount)

                else:
                    print('!amount')
                    pending_amount = int(total_amount) - int(p_obj.paid_amount)

                ph_obj.save()
                p_obj.payement_history.add(ph_obj)
                p_obj.save()
                return Response(
                    {
                        STATUS:True,
                        MESSAGE:msg,
                        "id":p_obj.id,
                        "total_amount":p_obj.total_amount,
                        "paid_amount":p_obj.paid_amount,
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

def updateStock(pid,amount):
    p_obj = Products.objects.filter(id = pid)
    if p_obj.exists():
        p_obj = p_obj.first()
        p_obj.stock = p_obj.stock + amount
        p_obj.save()

