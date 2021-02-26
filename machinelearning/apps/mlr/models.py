from django.db import models
from django_pandas.managers import DataFrameManager

class Dataset(models.Model):
    luas_lahan = models.IntegerField()
    jumlah_pokok = models.IntegerField()
    jumlah_tbs = models.IntegerField()
    umur = models.IntegerField()
    hasil_produksi = models.IntegerField()

    objects = DataFrameManager()

    def __int__(self):
        return self.hasil_produksi