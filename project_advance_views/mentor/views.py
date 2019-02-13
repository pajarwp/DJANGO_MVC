from django.shortcuts import render
from .models import Mentor
# Create your views here.
def mentor(request) :
    mentor = Mentor.objects.all ()
    return render(request, 'mentor/daftar_mentor.html',{'mentor':mentor})