from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpRequest
from .models import Product

# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request, 'index.html',{'products': products})

def new(request):
    return HttpResponse('New Products')


