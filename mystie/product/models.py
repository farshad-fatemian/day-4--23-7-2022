from distutils.command.upload import upload
from urllib import request
from django.db import models
from django.forms import CharField, DateTimeField, HiddenInput
from django.utils import timezone

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to="products/%Y/%m/%d/",blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    number = models.IntegerField(default=1)
    description = models.TextField(default="خالی",max_length=100)
    
    
    @property
    def dollar_amount(self):
        return "$%s" % self.price if self.price else ""
    
    @property
    def availability(self):
        return "%s" % "موجود" if self.available else "ناموجود"
   
    def __str__(self):
        return self.name
    
    
class comments(models.Model):
    product = models.ForeignKey(Product,related_name="comments1", on_delete=models.CASCADE )
    comment = models.TextField()
    writer = "ali"
    
    def __str__(self):
        return str(self.writer)+""+str(self.id)