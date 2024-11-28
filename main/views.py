from django.shortcuts import render

# Create your views here.
def master(request):

    return render(request,'dashboard.html')


def house_to_rent(request):
    return None


def rented_houses(request):
    return None


def fines(request):
    return None


def rent_house(request):
    return None