from django.urls import path
from products import views
from django.urls import re_path

urlpatterns = [
    path("products/", views.product_home_page),
    path("productid/<int:id>/<str:name>/<int:age>", views.product_id),
    re_path(r'^(?P<year>[0-9]{4})/$', views.show_year),
    path("productlist/", views.product_list),
    path("customerinfo/", views.buyer_info),
]
