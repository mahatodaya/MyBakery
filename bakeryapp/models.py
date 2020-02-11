from django.db import models
# from django.forms import ModelForm, Textarea
# from django.db import models

# Create your models here.

# class Users(models.Model):


class Products(models.Model):
     img = models.ImageField(upload_to='pics')
     name = models.CharField(max_length=100)
     price = models.IntegerField()