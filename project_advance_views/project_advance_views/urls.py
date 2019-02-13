from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('', include('blog.urls')),
    path('', include('mentor.urls')),
    path('', include('mentee.urls')),
    path('', include('author.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
