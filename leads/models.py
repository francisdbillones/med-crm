from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser

from agents.models import Agent


class Category(models.Model):
    name = models.CharField(max_length=20, null=True, blank=False)


class Lead(models.Model):
    first_name = models.CharField(max_length=20, null=True, blank=False)
    last_name = models.CharField(max_length=20, null=True, blank=False)
    email = models.EmailField(null=True, blank=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL)
    specialty = models.CharField()
    description = models.TextField()
    phone_number = models.CharField(max_length=15, null=True, blank=False, unique=True)
    profile_picture = models.ImageField(null=True, blank=True, upload_to="lead_pfps")

    date_added = models.DateField(null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(email__isnull=False) | models.Q(phone__isnull=False),
                name="email_or_phone_not_null",
            )
        ]


class Program(models.Model):
    name = models.CharField(max_length=30, null=True, blank=False)
    description = models.TextField(null=True, blank=False)


class LeadPlan(models.Model):
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)

    outlet_geolocation_url = models.URLField(null=True, blank=False)
    outlet_name = models.CharField(max_length=50, null=True, blank=False)
    outlet_description = models.TextField(null=True, blank=False)


class Schedule(models.Model):
    datetime = models.DateTimeField(null=True, blank=False)
    agent_plan = models.ForeignKey(LeadPlan, on_delete=models.SET_NULL)


class TargetProduct(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to="target_product_images")
