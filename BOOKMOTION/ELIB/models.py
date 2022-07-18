from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
import os
import uuid


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s-%s.%s" % (instance.slug ,uuid.uuid4(), ext)
    return os.path.join('books/', filename)


class Student(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    register = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)

    def __str__(self):
        return self.user.first_name+'['+str(self.register)+']'

    def get_name(self):
        return self.user.first_name

    def get_user_id(self):
        return self.user.id


    def __str__(self):
        return"{} -{}".format(self.book.title, self.user.username)





