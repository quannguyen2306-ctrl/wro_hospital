from django.shortcuts import render
from django.http import HttpResponse
from .models import medicine
# Create your views here.
def index(response, id):
    list  = medicine.objects.get(id=id)
    return HttpResponse("<h1>%s</h1>" %list.name)




