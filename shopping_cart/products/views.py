from django.shortcuts import render
from django.http import HttpResponse, request
from .data import buyers_record

# Create your views here.
def product_home_page(request):
    return render(request, "products/product_home_page.html")

def product_id(request, id, name, age):
    return HttpResponse(f"My product id is {id}, my product name is {name}, my product age is {age}.")

def show_year(request, year):
    return HttpResponse(f"The year is {year}.")

def product_list(request):
    class Product:
        def __init__(self, brand):
            self.brand = brand
           
    data = {
        "name" : "i phone 14",
        "price" : 1000,
        "age" : 21,
        "description" : "This is a new product",
        "is_available" : True,
        "product" : Product("Apple"),
        "list_of_features" : ["OLED Display", "A15 Bionic Chip", "5G Connectivity", "Face ID"],
    }
    return render(request, "product_list.html", {"product": data})
    # or
    # return render(request, "product_list.html", data)

def buyer_info(request):
    return render(request, "buyer_info.html", {"buyers": buyers_record})