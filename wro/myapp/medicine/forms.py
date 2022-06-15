from django import forms
from pyparsing import Char

class createNewMedicine(forms.Form):
    name = forms.CharField(label="Medicine's name: ", max_length=200)


    
