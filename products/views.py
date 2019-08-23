from django.shortcuts import render
from django.views import View
from .models import product_detail
# Create your views here.
class homeView(View):
    men_products = product_detail.objects.filter(product_for='men')
    women_products = product_detail.objects.filter(product_for='women')
    def get(self,request):
        return render(request,'products/home.html',{'men_products':self.men_products,'women_products':self.women_products})