from django.db import models


class Truck(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')


class DeliveryRequest(models.Model):
    loading_country = models.CharField(max_length=100)
    loading_po_code = models.CharField(max_length=100)
    requested_loading_date = models.DateField()
    delivery_country = models.CharField(max_length=100)
    delivery_po_code = models.CharField(max_length=100)
    delivery_date = models.DateField()
    ftl_ltl = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    pic_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
