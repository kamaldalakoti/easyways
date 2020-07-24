from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path('',views.home,name='home'),
    path('Home',views.home,name='home'),
    path('Hospital',views.hospital,name='hospital'),
    path('Dentist',views.dentist,name='dentist'),
    path('Search',views.search,name='search'),
    path('Options',views.options,name='options'),
    path('Shop',views.shop,name='shop'),
    path('Option_Shop',views.option_shop,name='option_shop'),
    path('Shop_Search',views.shop_search,name='shop_search'),
    path('Map',views.map,name='map'),
    path('Tour',views.tour,name='tour'),
    path('Index',views.index,name='index'),

]