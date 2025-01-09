from django.shortcuts import render

from main.models import House, House_info, Renting


# Create your views here.
def master(request):

    return render(request,'dashboard.html')


def house_to_rent(request):
    houses = House_info.objects.all()

    return render(request,'house_to_rent.html',{'houses':houses})


def rented_houses(request):
    rented_houses = Renting.objects.all()
    return render(request,'rented_houses.html',{'rented_items':rented_houses})


def fines(request):
    return render(request,'fines.html')


def rent_house(request,id):
    house_info = House_info.objects.filter(pk=id)
    housed = House.objects.all()

    return render(request,'rent_house.html',{"house":house_info,"housed":housed})