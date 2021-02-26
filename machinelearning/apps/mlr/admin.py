from django.contrib import admin

# Register your models here.
from import_export.admin import ImportExportModelAdmin
from .models import Dataset

@admin.register(Dataset)
class DatasetsAdmin(ImportExportModelAdmin):
    list_display = ("luas_lahan", "jumlah_pokok", "jumlah_tbs", "umur", "hasil_produksi")
    pass