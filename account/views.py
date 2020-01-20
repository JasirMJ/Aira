from django.db import transaction
from django.http import HttpResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.utils import json
from AiraPanel.global_variables import *
from rest_framework.generics import ListAPIView

from account.serializers import *

def index(request):
    return HttpResponse('Welcome to Aira , site is under developement')

class AccountGroupView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = AccountGroupSerializer

    def get_queryset(self):
        queryset = AccountGroup.objects.all()
        return queryset

    def post(self,request):
        username = self.request.user.username
        userid = self.request.user.id

        aira_obj = AiraAuthentication.objects.filter(user_id_id=self.request.user.id).first()
        print(aira_obj.type)
        branch_id = aira_obj.company_id.id
        company_id = aira_obj.branch_id.id
        print("company_id : ",company_id)
        print("branch_id : ",branch_id)

        # with transaction.atomic():
        serializer = AccountGroupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(companyId=company_id,branchId = branch_id)
        printCreate("AccountGroup")
        return Response(
            {
                STATUS: True,
                MESSAGE: "Data added",
                "Data": request.data
            }
        )

        # try:
        #     name = self.request.POST.get('name', '')
        #     parent = self.request.POST.get('parent', '')
        #     companyId = self.request.POST.get('companyid', 'null')
        #     branchId = self.request.POST.get('branchid', 'null')
        #
        #     if parent == "":
        #         # ag_obj = AccountGroup(
        #         #     name=name,
        #         #     companyId=companyId,
        #         #     branchId=branchId,
        #         # )
        #         # ag_obj.save()
        #         with transaction.atomic():
        #             AccountGroup.objects.create(
        #                 name=name,
        #                 companyId=companyId,
        #                 branchId=branchId,
        #             )
        #     else:
        #         # ag_obj = AccountGroup(
        #         #     name=name,
        #         #     companyId=companyId,
        #         #     branchId=branchId,
        #         # )
        #         # ag_obj.save()
        #         with transaction.atomic():
        #
        #             AccountGroup.objects.create(
        #                 name=name,
        #                 parent=parent,
        #                 companyId=companyId,
        #                 branchId=branchId,
        #             )
        #
        #
        #     return Response(
        #             {
        #                 STATUS: True,
        #                 MESSAGE: "Data added",
        #                 "Data": request.data
        #             }
        #         )
        # except Exception as e:
        #     printLineNo()
        #     return Response(
        #         {
        #             STATUS:False,
        #             MESSAGE:"Excepction "+str(e),
        #             "Line No":printLineNo()
        #         }
        #     )
        #
    def put(self,request):
        try:
            id =self.request.POST.get('id',"")
            if id == "" or not id:
                return Response(
                    {
                        STATUS:False,
                        MESSAGE:"Required id"
                    }
                )
            ag_obj = AccountGroup.objects.filter(id=id).first()
        except Exception as e:
            printLineNo()
            return Response(
                {
                    STATUS:False,
                    MESSAGE:"Excepction occured "+str(e),
                    "line no":printLineNo()
                }
            )

        aira_obj = AiraAuthentication.objects.filter(user_id_id=self.request.user.id).first()
        print(aira_obj.type)
        branch_id = aira_obj.company_id.id
        company_id = aira_obj.branch_id.id
        print("company_id : ", company_id)
        print("branch_id : ", branch_id)


        # with transaction.atomic():
        serializer = AccountGroupSerializer(ag_obj,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(companyId=company_id, branchId=branch_id)
        printUpdated("AccountGroup")
        return Response(
            {
                STATUS: True,
                MESSAGE: "Data updated",
                "Data": request.data
            }
        )

    def delete(self,request):
        try:
            id = self.request.POST.get('id', "")
            print(id)
            if id == "" or not id:
                AccountGroup.objects.all().delete()
                printDeleted("AccountGroup")
                return Response(
                    {
                        STATUS:True,
                        MESSAGE:"Deleted account group data",
                    }
                )
            else:
                id = id.split(",")

                AccountGroup.objects.filter(id__in=id).delete()
                printDeleted("AccountGroup")

                return Response(
                    {
                        STATUS:True,
                        MESSAGE:"account group deleted having id "+str(id),
                    }
                )
        except Exception as e:
            printLineNo()
            return Response(
                {
                    STATUS:False,
                    MESSAGE:str(e),
                    "line_no":printLineNo()
                }
            )


class AccountsView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = AccountsSerializer

    def get_queryset(self):
        queryset = Accounts.objects.all()
        return queryset

    def post(self,request):
        username = self.request.user.username
        userid = self.request.user.id

        aira_obj = AiraAuthentication.objects.filter(user_id_id=self.request.user.id).first()
        print(aira_obj.type)
        branch_id = aira_obj.company_id.id
        company_id = aira_obj.branch_id.id
        print("company_id : ",company_id)
        print("branch_id : ",branch_id)

        # with transaction.atomic():
        serializer = AccountsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(companyId=company_id,branchId = branch_id)
        printCreate("Accounts")
        return Response(
            {
                STATUS: True,
                MESSAGE: "Data added",
                "Data": request.data
            }
        )

        # try:
        #     name = self.request.POST.get('name', '')
        #     parent = self.request.POST.get('parent', '')
        #     companyId = self.request.POST.get('companyid', 'null')
        #     branchId = self.request.POST.get('branchid', 'null')
        #
        #     if parent == "":
        #         # ag_obj = AccountGroup(
        #         #     name=name,
        #         #     companyId=companyId,
        #         #     branchId=branchId,
        #         # )
        #         # ag_obj.save()
        #         with transaction.atomic():
        #             AccountGroup.objects.create(
        #                 name=name,
        #                 companyId=companyId,
        #                 branchId=branchId,
        #             )
        #     else:
        #         # ag_obj = AccountGroup(
        #         #     name=name,
        #         #     companyId=companyId,
        #         #     branchId=branchId,
        #         # )
        #         # ag_obj.save()
        #         with transaction.atomic():
        #
        #             AccountGroup.objects.create(
        #                 name=name,
        #                 parent=parent,
        #                 companyId=companyId,
        #                 branchId=branchId,
        #             )
        #
        #
        #     return Response(
        #             {
        #                 STATUS: True,
        #                 MESSAGE: "Data added",
        #                 "Data": request.data
        #             }
        #         )
        # except Exception as e:
        #     printLineNo()
        #     return Response(
        #         {
        #             STATUS:False,
        #             MESSAGE:"Excepction "+str(e),
        #             "Line No":printLineNo()
        #         }
        #     )
        #
    def put(self,request):
        try:
            id =self.request.POST.get('id',"")
            if id == "" or not id:
                return Response(
                    {
                        STATUS:False,
                        MESSAGE:"Required id"
                    }
                )
            a_obj = Accounts.objects.filter(id=id).first()
        except Exception as e:
            printLineNo()
            return Response(
                {
                    STATUS:False,
                    MESSAGE:"Excepction occured "+str(e),
                    "line no":printLineNo()
                }
            )

        aira_obj = AiraAuthentication.objects.filter(user_id_id=self.request.user.id).first()
        print(aira_obj.type)
        branch_id = aira_obj.company_id.id
        company_id = aira_obj.branch_id.id
        print("company_id : ", company_id)
        print("branch_id : ", branch_id)


        # with transaction.atomic():
        serializer = AccountsSerializer(a_obj,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(companyId=company_id, branchId=branch_id)
        printCreate("Accounts")
        return Response(
            {
                STATUS: True,
                MESSAGE: "Data updated",
                "Data": request.data
            }
        )

    def delete(self,request):
        try:
            id = self.request.POST.get('id', "")
            if id == "" or not id:
                Accounts.objects.all().delete()
                printDeleted("Accounts")
                return Response(
                    {
                        STATUS:True,
                        MESSAGE:"Deleted account group data",
                    }
                )
            else:
                id = id.split(",")

                Accounts.objects.filter(id__in=id).delete()
                printDeleted("Accounts")
                return Response(
                    {
                        STATUS:True,
                        MESSAGE:"account group deleted having id "+str(id),
                    }
                )
        except Exception as e:
            printLineNo()
            return Response(
                {
                    STATUS:False,
                    MESSAGE:str(e),
                    "line_no":printLineNo()
                }
            )

class GeneralLedgerView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = GeneralLedgersSerializer
    queryset = GeneralLedgers.objects.all().order_by('-id')