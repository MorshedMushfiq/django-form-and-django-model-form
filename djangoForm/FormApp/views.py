from django.shortcuts import render

from FormApp.forms import *
from FormApp.models import *

# Create your views here.

def formPage(req):
    
    form = StudentForm()
    if req.method == "POST":
        name = req.POST.get('name')
        email = req.POST.get('email')
        dept = req.POST.get('dept')
        StudentModel.objects.create(name=name, email=email, dept=dept)
    
    
    return render(req, 'forms.html', {"f":form})
