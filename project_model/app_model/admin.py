from django.contrib import admin
from .models import Mentee, BlogPost

# Register your models here.
my_model = [Mentee, BlogPost]
admin.site.register(my_model)