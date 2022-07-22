import django.db.models as models
from django.db.models import Q
from django.contrib.auth.models import AbstractUser


class Representative(AbstractUser):
    phone = models.CharField(max_length=20, null=True, blank=False)
    profile_picture = models.ImageField(
        upload_to="representative_pfps", null=True, blank=True
    )

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=Q(email__isnull=False) | Q(phone__isnull=False),
                name="representative_email_or_phone_not_null",
            )
        ]
