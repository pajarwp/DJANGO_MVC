from django.urls import path

from . import views

urlpatterns = [
    path('blog/', views.input_blog, name='blog'),
    path('new_blog/', views.new_blog, name='new_blog'),
    path('blog/<int:post_id>/', views.post_detail, name='post_detail')
]

