from django.db import models
from django.contrib.auth.models import AbstractUser


class Agent(AbstractUser):
    # fields already defined by AbstractUser:
    # username
    # first_name
    # last_name
    # email
    # is_staff
    # is_active
    # date_joined

    phone = models.CharField(
        max_length=15,
        null=True,
        blank=False,
        validators=[lambda s: all(c.isdigit() for c in s)],
    )
    profile_picture = models.ImageField(upload_to="agent_pfps", null=True, blank=True)

    def __str__(self):
        return self.user.email

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(email__isnull=False) | models.Q(phone__isnull=False),
                name="agent_email_or_phone_not_null",
            )
        ]
