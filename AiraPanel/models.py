from django.db import models

# Create your models here.

class Companies(models.Model):
    name = models.CharField(max_length=120,unique=True)

class Customers(models.Model):
    name = models.CharField(max_length=120,unique=True)

class Categories(models.Model):
    name = models.CharField(max_length=120,unique=True)

class SubCategories(models.Model):
    name = models.CharField(max_length=120,unique=True)

class Units(models.Model):
    name = models.CharField(max_length=120,unique=True)
    # measurement = models.CharField(max_length=120)

class Products(models.Model):
    pdt = models.CharField(max_length=100,unique=True)
    name = models.CharField(max_length=120,unique=True)
    hsn_code = models.CharField(max_length=120,null=True)
    hsn_group = models.CharField(max_length=120,null=True)
    item_name = models.CharField(max_length=120,null=True)

    #selling rules
    mrp = models.CharField(max_length=12,null=True)
    wholesale = models.CharField(max_length=12, null=True)
    sp = models.CharField(max_length=12, null=True)
    retail = models.CharField(max_length=12, null=True)
    branch = models.CharField(max_length=12, null=True)
    loading_charge = models.CharField(max_length=12, null=True)
    is_active = models.IntegerField()

    #details
    common_name = models.CharField(max_length=12, null=True)

    manufaturer = models.ManyToManyField(Companies)
    category = models.ManyToManyField(Categories)
    subcategory = models.ManyToManyField(SubCategories)
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




class ItemsInvoice(models.Model):
    invoiceId = models.CharField(max_length=20)
    product_Id = models.CharField(max_length=20)
    # customer = models.ManyToManyField(Customers)
    # company = models.ManyToManyField(Companies)
    item_price = models.CharField(max_length=20)
    tax = models.CharField(max_length=10)

class PayemetHistory(models.Model):
    invoice_id = models.CharField(max_length=12,null=True)
    date_of_payement = models.DateTimeField(null=False)
    amount =models.CharField(max_length=12,null=True)
    description =models.CharField(max_length=120,null=True)

    def __str__(self):
        return self.date_of_payement

class Invoices(models.Model):
    # invoiceid = models.CharField(max_length=12,null=True)
    customer = models.CharField(max_length=10,null=True)
    created = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=False)
    company = models.CharField(max_length=10,null=True)
    status = models.CharField(max_length=20,null=True)
    total_amount = models.CharField(max_length=12,null=True)
    paid_amount = models.CharField(max_length=12,null=True)
    # product = models.ManyToManyField(Products)
    items = models.ManyToManyField(ItemsInvoice,related_name="item_invoice")
    payement_history = models.ManyToManyField(PayemetHistory)

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





