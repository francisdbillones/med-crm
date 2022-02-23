from django.db import models
from django.db.models import Model


class Representative(Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=20)
    profile_picture = models.ImageField(upload_to="representative_pfps")


class Program(Model):
    name: str = models.CharField(max_length=50)
    description: str = models.TextField()


class Client(Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=20)
    specialty = models.CharField(max_length=100)
    office_latitude = models.FloatField()
    office_longitude = models.FloatField()
    profile_picture = models.ImageField(upload_to="client_pfps")


class ClientPlan(Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    representative = models.ForeignKey(Representative, on_delete=models.CASCADE)

    outlet_latitude = models.FloatField()
    outlet_longitude = models.FloatField()
    outlet_name = models.CharField(max_length=100)

    programs = models.ManyToManyField(Program)


class TargetProduct(Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.CharField(max_length=20)
    image = models.ImageField(upload_to="target_product_images")

