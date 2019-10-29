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

class Invoices(models.Model):
    # invoiceid = models.CharField(max_length=12,null=True)
    customer = models.ManyToManyField(Customers)
    created = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=False)
    company = models.ManyToManyField(Companies)
    status = models.CharField(max_length=12,null=True)
    total_amount = models.CharField(max_length=12,null=True)
    paid_amount = models.CharField(max_length=12,null=True)
    # product = models.ManyToManyField(Products)
    items = models.ManyToManyField(ItemsInvoice)



class PayemetHistory(models.Model):
    invoice_id = models.ForeignKey(Invoices,on_delete=models.CASCADE)
    date_of_payement = models.DateTimeField(auto_now_add=True)
    amount =models.CharField(max_length=12,null=True)



