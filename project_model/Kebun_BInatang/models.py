from django.db.models import CharField
from django.db.models import TextField
from django.db.models import IntegerField

from django.db import models

# Create your models here.
class Hewan(models.Model) :
    nama = models.CharField (max_length=255)
    spesies = models.CharField (max_length=25)
    berat = models.CharField (max_length=25)
    umur = models.IntegerField ()
    
    def __str__(self):
        return self.nama

class Kandang(models.Model) :
    nama = models.CharField (max_length=255)
    isi_kandang = models.CharField (max_length=25)
    luas_kandang = models.TextField (max_length=25)

    def __str__(self):
        return self.nama

class Penjaga(models.Model) :
    nama = models.CharField (max_length=255)
    nomor_telpon = models.IntegerField()
    jadwal_jaga = models.TextField (max_length=255)

    def __str__(self):
        return self.nama

class Pengunjung(models.Model) :
    nama = models.CharField (max_length=255)
    nomor_telpon = models.IntegerField ()
    hari_berkunjung = models.CharField (max_length=25)

    def __str__(self):
        return self.nama