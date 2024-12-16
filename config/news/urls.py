from django.contrib import admin
from django.urls import path
from .views import home, cars_by_brand, car_details

urlpatterns = [
    path('', home, name='home'),
    path('cars/<int:brand_id>/', cars_by_brand, name='cars_by_brand'),
    path('post/<int:car_id>/', car_details, name='car_details')
]