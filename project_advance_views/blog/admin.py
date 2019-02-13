from django.contrib import admin
from .models import Blog

# Register your models here.
my_model = [Blog]
admin.site.register(my_model)
fields = ( 'image_tag', )
readonly_fields = ('image_tag',)