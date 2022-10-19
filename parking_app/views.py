from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
from parking_app.models import Parkings, Users


# Create your views here.


def hello(request):
    return render(request, 'index.html', {'data':{
        'date': date.today(),
    }

    })


# def GetParkings(request):
#     return render(request, 'parkings.html', {'data': {
#         'date': date.today(),
#         'parkings': [
#             {'id': 1},
#             {'id': 2},
#             {'id': 3},
#         ]
#     }})


# def GetParking(request, id):
#     return render(request, 'parking.html', {'data' :{
#         'date': date.today(),
#         'id':id,
#
#     }})

def parkList(request):
    return render(
        request, 'parkings.html', {'data': {
            'date': date.today(),
            'parkings': Parkings.objects.all
        }}
    )


def GetParking(request, id):
    return render(request, 'parking.html', {'data': {
        'date': date.today(),
        'parking': Parkings.objects.filter(id=id)[0]
    }})
