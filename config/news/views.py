from django.shortcuts import render
from .models import Brand, Cars

def home(request):
    brands = Brand.objects.all()
    cars = Cars.objects.all()



    context = {
        'brands': brands,
        'cars': cars
    }

    return render(request, 'index.html', context)

def cars_by_brand(request, brand_id):
    brands = Brand.objects.all()
    cars = Cars.objects.filter(brand_id=brand_id)



    context = {
        'brands': brands,
        'cars': cars
    }


    return render(request, 'index.html', context)

def car_details(request, car_id):
    cars = Cars.objects.get(id=car_id)

    cars.views += 1
    cars.save()


    context = {
        'cars': cars
    }

    return render(request, 'details.html', context)