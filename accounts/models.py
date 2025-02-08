import re
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError


class CustomUser(AbstractUser):
    phone = models.CharField(
        max_length=20,
        unique=True,
        blank=True,
        null=True,
        default="+996 000 000 000"
    )

    def clean_phone(self):
        phone = self.phone.strip().replace(" ", "").replace("-", "")

        if not phone.startswith("+996"):
            phone = "+996" + phone

        if not re.match(r"^\+996\d{9}$", phone):
            raise ValidationError("Номер телефона должен быть в формате +996 XXX XXX XXX")

        self.phone = f"+996 {phone[4:7]} {phone[7:10]} {phone[10:13]}"
        return self.phone

    def save(self, *args, **kwargs):
        self.clean_phone()
        super().save(*args, **kwargs)
