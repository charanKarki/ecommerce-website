from django.contrib import admin
from .models import product_detail,user_ordered_product
# Register your models here.
admin.site.register(product_detail)

admin.site.register(user_ordered_product)