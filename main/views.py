from django.shortcuts import render, get_object_or_404

from main.models import House, House_info, Renting


# Create your views here.
def master(request):

    return render(request,'dashboard.html')


# def house_to_rent(request):
#     houses = House_info.objects.all()
#
#     return render(request,'house_to_rent.html',{'houses':houses})
def rent_house(request, id):
    print(f"Received id: {id}")
    house = get_object_or_404(House, pk=id)
    # Your view logic here
    return render(request, 'house_to_rent.html', {'house': house})

def rented_houses(request,id=None):
    rented = Renting.objects.all()
    return render(request,'rented_houses.html', {'rented_items':rented})


def fines(request):
    return render(request,'fines.html')


def rent_house(request,id):
    house_info = House_info.objects.filter(pk=id)
    housed = House.objects.all()

    return render(request,'rent_house.html',{"house":house_info,"housed":housed})