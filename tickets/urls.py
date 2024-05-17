from django.contrib import admin 
from django.urls import path
from tickets import views

app_name ='tickets'

urlpatterns = [
    path('', views.catalog, name='index'),
    path('product/', views.product, name='product'),
   #path('flights/', views.flights, name='flights' )
]