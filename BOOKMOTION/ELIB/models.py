from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    register = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)

    def __str__(self):
        return self.user.first_name+'['+str(self.register)+']'

    def get_name(self):
        return self.user.first_name

    def getuserid(self):
        return self.user.id






