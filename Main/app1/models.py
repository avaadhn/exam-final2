from django.db import models
from django.urls import reverse


class Products(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    price = models.PositiveIntegerField()
    label = models.CharField(max_length=30,null=True)
    image = models.ImageField(upload_to='static/Products')
    
    def get_absolute_url(self):
        return reverse('app1:detail',args=[self.id])
    
    def get_url(self):
        return reverse('app1:add_cart',args=[self.id])
    
    def __str__(self):
        return self.name
    
class Carts(models.Model):
    ip = models.GenericIPAddressField()
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    
    def get_url(self):
        return reverse('app1:del_cart',args=[self.pk])

    def __str__(self):
        return self.ip
    
