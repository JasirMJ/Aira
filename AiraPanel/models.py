from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django_bulk_update.manager import BulkUpdateManager


class AccountGroup(models.Model):
    name = models.CharField(max_length=100,unique=True)
    parent = models.ForeignKey('self',on_delete=models.PROTECT,null=True)
    companyId = models.CharField(max_length=20,null=True)
    branchId = models.CharField(max_length=20,null=True)

class Accounts(models.Model):
    name = models.CharField(max_length=100,unique=True)
    parent = models.ForeignKey(AccountGroup,on_delete=models.PROTECT)
    description = models.TextField(null=True)
    companyId = models.CharField(max_length=20,null=True)
    branchId = models.CharField(max_length=20,null=True)







class Counter(models.Model):
    name = models.CharField(max_length=120,null=False)

class Branch(models.Model):
    name = models.CharField(max_length=120,null=False)
    counter_id = models.ManyToManyField(Counter)

class Companies(models.Model):
    name = models.CharField(max_length=120,null=False)
    place = models.CharField(max_length=120,null=False)
    branch_id = models.ManyToManyField(Branch)
    company_of = models.CharField(max_length=255,null=True)

class AiraAuthentication(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.PROTECT,null=True,related_name='user_details')
    company = models.ManyToManyField(Companies)
    company_id = models.ForeignKey(Companies,on_delete=models.PROTECT,null=True,related_name="companyid")
    branch_id = models.ForeignKey(Branch,on_delete=models.PROTECT,null=True)
    counter_id = models.ForeignKey(Counter,on_delete=models.PROTECT,null=True)
    type = models.CharField(max_length=20)


    # is_active = models.BooleanField(
    #     default=True,
    #     help_text=(
    #         'Designates whether this user should be treated as active. '
    #         'Unselect this instead of deleting accounts.'
    #     ),
    # )
#
# class asd(models.Model):
#     name = models.CharField(max_length=120,unique=True,null=False)
#




class Customers(models.Model):
    name = models.CharField(max_length=120,unique=True)
    aira_code = models.CharField(max_length=120,unique=True,null=True)
    address = models.CharField(max_length=120,null=True)
    country = models.CharField(max_length=120,null=True)
    state = models.CharField(max_length=120,null=True)
    city_one = models.CharField(max_length=120,null=True)
    city_two = models.CharField(max_length=120,null=True)
    phone = models.CharField(max_length=20,null=True)
    mobile = models.CharField(max_length=20,null=True)
    job_position = models.CharField(max_length=100,null=True)
    email = models.EmailField(null=True)

    company = models.ForeignKey(Companies,on_delete=models.CASCADE,null=True)
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE,null=True)

class Categories(models.Model):
    name = models.CharField(max_length=120,unique=True)
    parent = models.ForeignKey("self",on_delete=models.PROTECT,null=True,related_name="subcategory")


class SubCategories(models.Model):
    name = models.CharField(max_length=120,unique=True)

class Units(models.Model):
    name = models.CharField(max_length=120,unique=True)
    # measurement = models.CharField(max_length=120)

class Products(models.Model):
    # pdt = models.CharField(max_length=100,unique=True)
    name = models.CharField(max_length=120,unique=True)
    hsn_code = models.CharField(max_length=120,null=True)
    hsn_group = models.CharField(max_length=120,null=True)
    item_name = models.CharField(max_length=120,null=True)

    #selling rules
    mrp = models.CharField(max_length=12,null=True)
    wholesale = models.CharField(max_length=12, null=True)
    sp = models.CharField(max_length=12, null=True)
    retail = models.CharField(max_length=12, null=True)
    # branch = models.CharField(max_length=12, null=True)
    loading_charge = models.CharField(max_length=12, null=True)
    is_active = models.IntegerField()

    #details
    common_name = models.CharField(max_length=12, null=True)
    manufaturer = models.ManyToManyField(Companies)
    category = models.ManyToManyField(Categories)
    # subcategory = models.ManyToManyField(SubCategories)
    unit = models.ManyToManyField(Units)

    reorder_level = models.IntegerField( null=True)
    rack = models.CharField(max_length=12, null=True)
    # packing = models.CharField(max_length=12, null=True)
    max_order_level = models.CharField(max_length=12, null=True)
    tax_group = models.CharField(max_length=12,null=True)
    tax_schedule = models.CharField(max_length=12,null=True)
    gst = models.CharField(max_length=12,null=True)
    sgst = models.CharField(max_length=12,null=True)
    igst = models.CharField(max_length=12,null=True)
    cgst = models.CharField(max_length=12,null=True)
    cess = models.CharField(max_length=12,null=True)
    additional_cess = models.CharField(max_length=12,null=True)
    second_name = models.CharField(max_length=12,null=True)

    stock = models.FloatField(default=0.0)

    objects = BulkUpdateManager()

    branch = models.ForeignKey(Branch,on_delete=models.CASCADE,null=True,related_name="product_branch")
    company = models.ForeignKey(Companies,on_delete=models.CASCADE,null=True,related_name="product_company")

# class ItemsInvoice(models.Model):
#     invoiceId = models.CharField(max_length=20)
#     product_Id = models.ForeignKey(Products,on_delete=models.SET_NULL,blank=True,null=True,related_name='iteminvoice_products')
#     # customer = models.ManyToManyField(Customers)
#     # company = models.ManyToManyField(Companies)
#     item_price = models.CharField(max_length=20)
#     tax = models.CharField(max_length=10)

class Items_relation(models.Model):
    invoice_id = models.CharField(max_length=20,null=True)
    sales_id = models.CharField(max_length=20,null=True)
    product_Id = models.ForeignKey(Products,on_delete=models.SET_NULL,blank=True,null=True,related_name='item_products')
    product_name = models.CharField(max_length=255,null=True)
    qty = models.FloatField(null=True)
    item_price = models.CharField(max_length=20,null=True)
    tax = models.CharField(max_length=100,null=True)
    tax_amount = models.CharField(max_length=100,null=True)

    item_code = models.CharField(max_length=120,null=True)
    unit_price = models.CharField(max_length=120,null=True)
    discount = models.CharField(max_length=120,null=True)
    net_amount = models.CharField(max_length=120,null=True)

class PayemetHistory(models.Model):
    invoice_id = models.CharField(max_length=12,null=True)
    date_of_payement = models.DateTimeField(null=False)
    amount =models.CharField(max_length=12,null=True)
    description =models.CharField(max_length=120,null=True)

    def __str__(self):
        return self.date_of_payement

# class Type_of_voucher(models.Model):
#     created = models.DateTimeField(auto_now_add=True)
#     modified = models.DateTimeField(auto_now_add=True)
#     unique_id = models.CharField(max_length=255,null=True)
#     type = models.CharField(max_length=10,null=True)
#     status = models.CharField(max_length=10,null=True)

class History(models.Model):
    # sales_id = models.ForeignKey(Sales, on_delete=models.CASCADE)
    # invoice_id = models.ForeignKey(Sales, on_delete=models.CASCADE)

    sales_id = models.CharField(max_length=20,null=True)
    invoice_id = models.CharField(max_length=20,null=True)
    type = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(null=True, blank=True)
    description = models.CharField(max_length=255, null=True)

class Sales(models.Model):
    customer = models.ForeignKey(Customers, on_delete=models.SET_NULL, blank=True, null=True,
                                 related_name='sales_customer')
    company = models.ForeignKey(Companies, on_delete=models.SET_NULL, blank=True, null=True,
                                related_name='sales_company')
    created = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=False)
    total_amount = models.CharField(max_length=12, null=True)
    items = models.ManyToManyField(Items_relation, related_name="sales_item")
    status = models.CharField(max_length=20, null=True)
    invoice_status = models.CharField(max_length=20, null=True)
    history = models.ManyToManyField(History)

class Invoices(models.Model):
    # invoiceid = models.CharField(max_length=12,null=True)
    customer = models.ForeignKey(Customers,on_delete=models.SET_NULL,blank=True,null=True,related_name='invoice_customer')
    company = models.ForeignKey(Companies,on_delete=models.SET_NULL,blank=True,null=True,related_name='invoice_company')
    created = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=False)
    total_amount = models.CharField(max_length=12,null=True)
    paid_amount = models.CharField(max_length=12,null=True)
    items = models.ManyToManyField(Items_relation,related_name="invoice_item")
    payement_history = models.ManyToManyField(PayemetHistory)
    status = models.CharField(max_length=20, null=True)
    history = models.ManyToManyField(History)
    type = models.CharField(max_length=20,null=False)

    counterid = models.ForeignKey(Counter, on_delete=models.PROTECT,null=True)
    branchid = models.ForeignKey(Branch, on_delete=models.PROTECT,null=True)
    companyid = models.ForeignKey(Companies, on_delete=models.PROTECT,null=True)


class ItemsBilling(models.Model):
    billingid = models.CharField(max_length=20)
    product_Id = models.CharField(max_length=20)
    customer = models.ManyToManyField(Customers)
    company = models.ManyToManyField(Companies)
    item_price = models.CharField(max_length=20)
    tax = models.CharField(max_length=10)
    amount = models.FloatField(max_length=10)

class Billing(models.Model):
    payer = models.CharField(max_length=10)
    payee = models.CharField(max_length=10)
    items = models.ManyToManyField(ItemsBilling)
#
class Purchase_Items_relation(models.Model):
    contract_id = models.CharField(max_length=20, null=True)
    purchase_id = models.CharField(max_length=20, null=True)
    product_Id = models.ForeignKey(Products, on_delete=models.SET_NULL, blank=True, null=True,
                                   related_name='purchase_products')
    item_price = models.CharField(max_length=20, null=True)
    tax = models.CharField(max_length=10, null=True)



class PurchaseContracts(models.Model):
    items = models.ManyToManyField(Purchase_Items_relation)
    contract_id = models.CharField(max_length=20,null=True)
    vendors = models.ManyToManyField(Customers)
    created = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True)

class PurchasePayemetHistory(models.Model):
    purchase_id = models.CharField(max_length=12,null=True)
    date_of_payement = models.DateTimeField(null=False)
    amount =models.CharField(max_length=12,null=True)
    description =models.CharField(max_length=120,null=True)

    def __str__(self):
        return self.date_of_payement

class PurchaseOrder(models.Model):
    items = models.ManyToManyField(Purchase_Items_relation)
    contract_referance = models.CharField(max_length=20, null=True)
    vendors = models.ManyToManyField(Customers)
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20,null=True)
    billing_status = models.CharField(max_length=20,null=True)
    vendor_referance = models.CharField(max_length=20,null=True)
    purchase_by = models.CharField(max_length=20,null=True)
    payement_history = models.ManyToManyField(PurchasePayemetHistory)
    total_amount = models.CharField(max_length=12, null=True)
    paid_amount = models.CharField(max_length=12, null=True)

    company = models.ForeignKey(Companies,on_delete=models.PROTECT)
    branch = models.ForeignKey(Branch,on_delete=models.PROTECT)
    # taxes = models.ManyToManyField()
    # taxes = models.ManyToManyField()

class Inventory(models.Model):
    itemid = models.ForeignKey(Products, on_delete=models.PROTECT)
    item_in = models.FloatField(default=0.0)
    item_out = models.FloatField(default=0.0)
    type = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)
    # quantity = models.FloatField()
    # price = models.FloatField()
    unit_price = models.FloatField()
    barcodeid = models.CharField(max_length=50,null=True)

    branch = models.ForeignKey(Branch,on_delete=models.CASCADE,null=True)

class Tax(models.Model):
    name = models.CharField(max_length=120)
    tax_percentage = models.CharField(max_length=20)
    description = models.CharField(max_length=255,null=True)
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE)


class PdtTaxMapping(models.Model):
    pdt_code = models.CharField(max_length=255)
    gst = models.ManyToManyField(Tax,related_name="gst_tax")
    igst = models.ManyToManyField(Tax,related_name="igst_tax")
    vat = models.ManyToManyField(Tax,related_name="vat_tax")
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE,null=True)

class GeneralLedgers(models.Model):
    transactionId = models.CharField(max_length=255)
    transactionType = models.CharField(max_length=50)
    createdAt = models.DateTimeField(auto_now_add=True)
    creditBy = models.ForeignKey(Accounts,on_delete=models.CASCADE,related_name="credit")
    debitBy = models.ForeignKey(Accounts,on_delete=models.CASCADE,related_name="debit")
    amount = models.FloatField()
    taxes = models.ManyToManyField(Tax)
    companyId = models.CharField(max_length=20)
    branchId = models.CharField(max_length=20)
    counterId = models.CharField(max_length=20,null=True)
