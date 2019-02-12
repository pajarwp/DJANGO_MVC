from django.urls import path

from . import views

urlpatterns = [
    path('blog/', views.input_blog, name='blog'),
]
