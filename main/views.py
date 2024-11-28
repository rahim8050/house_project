from django.shortcuts import render

# Create your views here.
def master(request):

    return render(request,'dashboard.html')


def house_to_rent(request):
    return render(request,'house_to_rent.html')


def rented_houses(request):
    return render(request,'rented_houses.html')


def fines(request):
    return render(request,'fines.html')


def rent_house(request):
    return render(request,'rent_house.html')