from django.db.models import CharField
from django.db.models import TextField
from django.db.models import IntegerField
from django.db.models import ForeignKey
from django.db.models import ImageField

from django.utils import timezone


from django.db import models

class Mentee(models.Model) :
    nama_lengkap = models.CharField (max_length=255)
    gambar = models.ImageField ()
    status = models.TextField (max_length=255)

    def __str__(self):
        return self.nama_lengkap