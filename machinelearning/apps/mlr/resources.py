from import_export import resources
from .models import Dataset

class DatasetResource(resources.ModelResource):
    class Meta:
        model = Dataset