from django.db import models
from django.db.models import Model, Q
from django.contrib.auth.models import User


class Representative(Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    profile_picture = models.ImageField(upload_to="representative_pfps")

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=Q(email__isnull=False) | Q(phone__isnull=False),
                name="representative_email_or_phone_not_null",
            )
        ]


class Program(Model):
    name = models.CharField(max_length=50)
    description = models.TextField()


class Client(Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    specialty = models.CharField(max_length=100)
    office_latitude = models.FloatField(null=True, blank=True)
    office_longitude = models.FloatField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to="client_pfps", null=True, blank=True)

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=Q(email__isnull=False) | Q(phone__isnull=False),
                name="client_email_or_phone_not_null",
            )
        ]


class Schedule(Model):
    monday = models.BooleanField(default=False, blank=True)
    tuesday = models.BooleanField(default=False, blank=True)
    wednesday = models.BooleanField(default=False, blank=True)
    thursday = models.BooleanField(default=False, blank=True)
    friday = models.BooleanField(default=False, blank=True)
    satuday = models.BooleanField(default=False, blank=True)
    sunday = models.BooleanField(default=False, blank=True)


class ClientPlan(Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    representative = models.ForeignKey(Representative, on_delete=models.CASCADE)

    outlet_latitude = models.FloatField(null=True, blank=True)
    outlet_longitude = models.FloatField(null=True, blank=True)
    outlet_name = models.CharField(max_length=100, null=True, blank=True)

    programs = models.ManyToManyField(Program)

    schedule = models.OneToOneField(Schedule, on_delete=models.CASCADE, null=True, blank=True)


class TargetProduct(Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    image = models.ImageField(upload_to="target_product_images")

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=Q(price__isnull=False) & Q(price__gte=0),
                name="target_product_price_positive",
            )
        ]

