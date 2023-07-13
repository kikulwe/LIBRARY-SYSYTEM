from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

class User(AbstractUser):

    objects = UserManager()

    class Role(models.TextChoices):
        STAFF = "STAFF", 'Staff'
        STUDENT = "STUDENT", 'Student'

    base_account_type = Role.STAFF

    account_type = models.CharField(
        verbose_name="Account Type",
        max_length=50,
        choices=Role.choices
    )

    def save(self, *args, **kwargs):
        if not self.pk:
            self.account_type = self.base_account_type

        if self.account_type == 'STAFF':
            self.is_staff = True

        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.get_username()

class StudentProfile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    reg_no = models.CharField('Registration Number', unique=True, max_length=30, blank=True, null=True)

class Student(User):

    base_account_type = User.Role.STUDENT
    class Meta:
        proxy = True
        