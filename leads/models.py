from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser

from agents.models import Agent
from djcrm.helpers import all_is_digit


class Category(models.Model):
    name = models.CharField(max_length=20, null=True, blank=False)

    def __str__(self):
        return self.name


class Lead(models.Model):
    first_name = models.CharField(max_length=20, null=True, blank=False)
    last_name = models.CharField(max_length=20, null=True, blank=False)
    email = models.EmailField(null=True, blank=False)
    age = models.IntegerField(null=True, blank=False)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    specialty = models.CharField(max_length=100, null=True, blank=False)
    description = models.TextField(null=False, blank=True, default="No description")
    phone = models.CharField(
        max_length=15,
        null=True,
        blank=False,
        validators=[all_is_digit],
    )
    profile_picture = models.ImageField(null=True, blank=True, upload_to="lead_pfps")

    date_added = models.DateField(null=True)
    converted_date = models.DateField(null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def display_first_name(self):
        return str(self.first_name) if self.first_name else ""

    def display_last_name(self):
        return str(self.last_name) if self.last_name else ""

    def display_age(self):
        if self.age is None:
            return "Age not specified"
        return f"<strong>{self.age}</strong>"

    def display_email(self):
        if self.email is None:
            return "Email not specified"
        return f"<strong>{self.email}</strong>"

    def display_phone(self):
        if self.phone is None:
            return "Phone number not specified"
        return f"<strong>{self.phone}</strong>"

    def display_description(self):
        if self.description is None:
            return "No description"
        return str(self.description)

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(email__isnull=False) | models.Q(phone__isnull=False),
                name="lead_email_or_phone_not_null",
            )
        ]


class Program(models.Model):
    name = models.CharField(max_length=30, null=True, blank=False)
    description = models.TextField(null=True, blank=False)

    def __str__(self):
        return self.name


class LeadPlan(models.Model):
    lead = models.ForeignKey(Lead, on_delete=models.PROTECT)
    agent = models.ForeignKey(Agent, on_delete=models.PROTECT)

    outlet_geolocation_url = models.URLField(null=True, blank=False)
    outlet_name = models.CharField(max_length=50, null=True, blank=False)
    outlet_description = models.TextField(null=True, blank=False)

    def __str__(self):
        return f"LeadPlan {self.lead} with agent {self.agent}"


class Schedule(models.Model):
    datetime = models.DateTimeField(null=True, blank=False)
    agent_plan = models.ForeignKey(LeadPlan, on_delete=models.CASCADE)

    def __str__(self):
        return f"Schedule for {self.agent_plan} on {self.datetime.strftime('%d-%b-%Y at %H:%M')}"


class TargetProduct(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to="target_product_images")
