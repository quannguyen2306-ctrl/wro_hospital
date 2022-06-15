from django import forms
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import medicine, PatientMedicine
from .forms import createNewMedicine
# Create your views here.
import json 

def index(response, id):
    list  = medicine.objects.get(id=id)
    return render(response, 'medicine/base.html', {'name': list.name})

def home(response):
    m = medicine.objects
    mydict = {
        'name1': m.get(id=1),
        'name2': m.get(id=2),
        'name3': m.get(id=3),
    }
    alreadyPrint = []
    # return render(response, 'medicine/home.html', mydict)
    id = 1
    while True:
        f = open("/Users/nguyenhoangquan/Documents/WRO&SAMSUNG/Coding/wro/myapp/medicine/templates/medicine/data.json")

        data = json.load(f)
        for i in data["prescription"]:
            if i not in alreadyPrint:
                print(i)
                alreadyPrint.append(i)
                patient = PatientMedicine.objects
                PatientMedicine(id,i).save()
                id +=1
            else:
                continue
        # return render(response, 'medicine/home.html', {})


    


def create(response):
    if response.method == "POST":
        forms = createNewMedicine(response.POST)

        if forms.is_valid():
            n = forms.cleaned_data["name"]
            m = medicine(name=n)
            m.save()
        
        return HttpResponseRedirect("/%i" %m.id)
    forms = createNewMedicine()
    return render(response, 'medicine/create.html', {'form': forms})




