from django.db import models
from django.contrib.auth.models import AbstractUser


class Student(AbstractUser):
    reg_no = models.CharField('Identity Card Number', unique=True, max_length=30, blank=True, null=True)

    # USERNAME_FIELD = 'reg_no'

    def __str__(self) -> str:
        if not self.get_full_name():
            return self.get_username()
        return self.get_full_name()