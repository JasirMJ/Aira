import json

from django.contrib.auth.hashers import make_password
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from .models import *
from .global_variables import *
from rest_framework.views import APIView
from .serializers import *

from rest_framework.authtoken.models import Token
from django.contrib.auth import login as django_login, logout as django_logout


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

class LoginView(ListAPIView):
    def post(self,request):
        print(request.data)
        serializer = LoginSerializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data['user']

            print(django_login(request, user))
            token, created = Token.objects.get_or_create(user=user)
            print("token  ",token)
            print("created ",created)
            return Response(
                {
                    STATUS: True,
                    'Token': 'Token '+token.key
                },
                status=200
            )
        except Exception as e:
            print("Excepction occured ################### : ", e)
            return Response(
                {
                    'status': False,
                    'Message': 'Invalid user',
                }
            )


class RegisterView(ListAPIView):
    serializer_class = RegisterViewSerializer

    # permission_classes = (IsAdminUser,)
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        if self.request.user.is_staff == True:
            qs = AiraAuthentication.objects.all().prefetch_related('user_id').order_by('-id')
        else:
            qs = AiraAuthentication.objects.filter(user_id_id=self.request.user.id).prefetch_related('user_id').order_by('-id')
        return qs

    def post(self,request):
        # print(self.request.user.is_staff)
        fname = self.request.POST.get('fname', '')
        lname = self.request.POST.get('lname', '')
        email = self.request.POST.get('email', '')
        username = self.request.POST.get('username', '')

        password = 123123

        if username == "" or not username:
            return Response({
                STATUS: False,
                MESSAGE: "required username"
            })

        if email == "" or not email:
            return Response({
                STATUS: False,
                MESSAGE: "required email"
            })

        user_obj = User()
        user_obj.username = username
        user_obj.first_name = fname
        user_obj.last_name = lname
        user_obj.email = email
        user_obj.password = make_password(password)

        try:

            if self.request.user.is_staff == True:
                # return Response(True)
                ''' if the user is super admin , he can create new company and a new user'''
                type = 'company'
                company = self.request.POST.get('company','')
                if company == '' or not company:
                    return Response(
                        {
                            STATUS : False,
                            MESSAGE : "required company"
                        }
                    )

                c_obj = Companies(
                    name=company,
                )
                c_obj.save()
                print("Companies : Created :",c_obj)

                user_obj.save()
                print("User : Creted", user_obj)

                auth_obj = AiraAuthentication()
                auth_obj.user_id = user_obj
                auth_obj.type = type
                auth_obj.save()
                print("AiraAuthentication : created :",auth_obj)
                auth_obj.company_id.add(
                    c_obj
                )
                print("AiraAuthentication : ",c_obj," added to ","AiraAuthentication.company_id")

                return Response(
                    {
                        STATUS:True,
                        MESSAGE:"Hi Admin! New "+type+" created :"+str(company),
                        'created by':self.request.user.username
                    }
                )

            elif self.request.user.is_staff == False:
                ''' if the user is company , he can create new branch and a new counter'''
                aira_obj = AiraAuthentication.objects.filter(user_id_id=self.request.user.id)
                if aira_obj.exists:
                    if aira_obj.first().type:
                        print(aira_obj.first().type)
                        user_type = aira_obj.first().type
                else:
                    return Response(
                        {
                            STATUS:False,
                            MESSAGE:"user not found",
                            CODE:"dqwd12ccs"
                        }

                    )

                type = self.request.POST.get('type', '')
                # company = self.request.POST.get('company', '')
                branch_name = self.request.POST.get('branch_name', 'branch01')
                counter_name = self.request.POST.get('counter_name', 'counter01')

                if type == "" or not type:
                    return Response(
                        {
                            STATUS : False,
                            MESSAGE : "required type as 'branch' or 'counter' got type as :"+type,
                            CODE:"4532g51",
                        }
                    )
                if branch_name == '' or not branch_name:
                    return Response(
                        {
                            STATUS : False,
                            MESSAGE : "required branch_name"
                        }
                    )

                b_obj = Branch(
                    name=branch_name
                )

                counter_obj = Counter(
                    name=counter_name
                )

                if type == 'branch':
                    '''Create Branch'''
                    try:
                        print("Create Branch")
                        obj = AiraAuthentication.objects.filter(user_id_id=self.request.user.id).first()
                        print("Company id : ",obj.company_id.first().id)
                        company_id = obj.company_id.first().id
                        c_obj = Companies.objects.get(
                            id=company_id,
                        )
                        print(c_obj)


                        # return Response(type)

                        counter_obj.save()
                        print("Counter : created :", counter_obj)

                        b_obj.save()
                        print("Branch : created :", b_obj)

                        c_obj = Companies.objects.get(
                            id=company_id,
                        )

                        user_obj.save()
                        print("User : Creted",user_obj)

                        auth_obj = AiraAuthentication()
                        auth_obj.user_id = user_obj
                        auth_obj.type = type
                        auth_obj.save()
                        print("AiraAuthentication : created :", auth_obj)

                        auth_obj.company_id.add(
                            c_obj
                        )
                        c_obj.branch_id.add(
                            b_obj
                        )
                        b_obj.counter_id.add(
                            counter_obj
                        )

                        return Response(
                            {
                                STATUS: True,
                                MESSAGE: "Hi " + self.request.user.username + "! New" + type + "created :" + str(
                                    branch_name),
                                'created by': self.request.user.username

                            }
                        )
                    except Exception as e:
                        if auth_obj:
                            auth_obj.delete()
                        if user_obj:
                            user_obj.delete()

                        return Response(
                            {
                                STATUS: False,
                                MESSAGE: "Excepction occured :"+str(e),
                                "Line no": str(format(sys.exc_info()[-1].tb_lineno)),
                                CODE: 'd2t5g1a'
                            }
                        )

                elif type == "counter" :
                    '''Create Counter and add it to a branch'''
                    print("Create Counter")

                    obj = AiraAuthentication.objects.filter(user_id_id=self.request.user.id).first()
                    print("Company id : ", obj.company_id.first().id)
                    branch_obj = obj.company_id.first().branch_id.first()

                    return Response({
                        "branch":branch_obj.id,
                        "branch name":branch_obj.name,
                    })

                    if obj.type != "branch":
                        print("not branch")
                        return Response(
                            {
                                STATUS:False,
                                MESSAGE:"only branch can create many counter, please login in as a branch",
                                CODE:"98huh5"
                            }
                        )

                    # return Response(
                    #     {
                    #         STATUS:True,
                    #         MESSAGE:obj.company_id.first().id,
                    #         "type":obj.type,
                    #         "branch id":obj.company_id.first().branch_id.first().id,
                    #
                    #     }
                    # )

                    try:
                        print("Branch id : ", branch_obj)

                        counter_obj.save()
                        print("Counter : created :", counter_obj)

                        user_obj.save()
                        print("User : Creted", user_obj)

                        auth_obj = AiraAuthentication()
                        auth_obj.user_id = user_obj
                        auth_obj.type = type
                        auth_obj.save()
                        print("AiraAuthentication : created :", auth_obj)

                        branch_obj.counter_id.add(
                            counter_obj
                        )

                        return Response(
                            {
                                STATUS: True,
                                MESSAGE: "Hi " + self.request.user.username + "! New" + type + "created :"+str(counter_name),
                                'created by': self.request.user.username
                            }
                        )
                    except Exception as e:
                        print("Excepction :",str(e))
                        if auth_obj:
                            auth_obj.delete()
                            print("AiraAuthentication : Deleted")
                        if user_obj:
                            user_obj.delete()
                            print("User : Deleted")

                        if b_obj:
                            b_obj.delete()
                            print("Branch : Deleted")


                        return Response(
                            {
                                STATUS: False,
                                MESSAGE: "Excepction occured :" + str(e),
                                "Line no": str(format(sys.exc_info()[-1].tb_lineno)),
                                CODE: 'd2t5g1a'
                            }
                        )

        except Exception as e:
            print("Excepction :" + str(e) + " Line no :" + str(format(sys.exc_info()[-1].tb_lineno)))
            #
            # if c_obj:
            #     try:
            #         c_obj.delete()
            #         print("company ", c_obj, " deleted")
            #     except Exception as e:
            #         print(str(e))
            #
            # if user_obj:
            #     try:
            #         user_obj.delete()
            #         print("user ", user_obj, " deleted")
            #     except Exception as e:
            #         print(str(e))

            return Response(
                {
                    STATUS:False,
                    "Exception":str(e),
                    MESSAGE:str(format(sys.exc_info()[-1].tb_lineno)),
                }
            )

    def delete(self,request):
        user_id = self.request.POST.get('user_id','')
        if user_id == "" :
            print("User : All user delete")
            msg = "User : All users delete"
            print(AiraAuthentication.objects.all().delete())
        else:
            print(" User : ",user_id," delete")
            msg = " User : "+str(user_id)+" deleted"
            print(AiraAuthentication.objects.get(user_id_id=user_id).delete())

        return Response(
            {
                STATUS:True,
                MESSAGE:msg,
            }
        )


class AiraUser(ListAPIView):
    serializer_class = UserSerializers
    def get_queryset(self):
        qs = User.objects.all()
        return qs

    def delete(self,request):
        id = self.request.POST.get('id','')
        if id == '':
            print(User.objects.all().exclude(is_staff=True).delete())
            msg = "User : All users deleted except admin"

        else:
            print(User.objects.filter(id=id).exclude(is_staff=True).delete())
            msg = "User : users "+str(id)+" deleted except admin "

        return Response(
            {
                STATUS:True,
                MESSAGE:msg
            }
        )

