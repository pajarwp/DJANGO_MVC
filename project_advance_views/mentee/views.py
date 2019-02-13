from django.shortcuts import render
from .models import Mentee


# Create your views here.
def mentee(request) :
    mentee = Mentee.objects.all()
    return render(request, 'mentee/daftar_mentee.html',{'mentee':mentee})