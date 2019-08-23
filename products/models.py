from django.db import models
from django.contrib.auth.models import User
import os
# Create your models here.

# function for rename upload image
def changeName(instance,filename):
    ext = filename.split('.')[-1]
    filename = f'img.{ext}'
    path = f'products/{instance.product_name}'
    return os.path.join(path,filename)


class product_detail(models.Model):
  
    product_name = models.CharField(max_length=40)
    product_for = models.CharField(max_length =10)
    product_price= models.FloatField()
    product_img = models.ImageField(upload_to=changeName)

    def __str__(self):
        return f'{self.product_name}'



class user_ordered_product(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(product_detail,on_delete=models.CASCADE)
    count = models.IntegerField()

    def __str__(self):
        return f'{self.user.username} order'