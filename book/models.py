from django.db import models
from rest_framework import serializers
# Create your models here.
from distutils.command.upload import upload
from django.db import models

# Create your models here.
avaibility=(
    ('In stock','In stock'),
    ('Out of stock','Out of stock'),
)

class Books(models.Model):
    book=models.CharField(max_length=60)
    author= models.CharField(max_length=50)
    about= models.CharField(max_length=1000)
    status= models.CharField(max_length=20,choices=avaibility)
    price=models.IntegerField()
    rating=models.IntegerField()
    view=models.FileField(upload_to="media")

    def __str__(self):
        return self.book


gender=(
    ('Male','Male'),
    ('Female','Female'),

)


class RegisterAdmin(models.Model):
    username=models.CharField(max_length=30)
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
    pass1=models.CharField(max_length=20)
    pass2=models.CharField(max_length=20)
    gender=models.CharField(max_length=8,choices=gender,default="")


    def __str__(self):
        return self.username


class RegisterUser(models.Model):
    username=models.CharField(max_length=30)
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
    pass1=models.CharField(max_length=20)
    pass2=models.CharField(max_length=20)
    gender=models.CharField(max_length=8,choices=gender,default="")


    def __str__(self):
        return self.username