import datetime
from django.conf import settings
import os
from django.http import HttpResponse, Http404
from sistema_fcc_api.file_storage.file_system_storage import FileSystemStorage
from sistema_fcc_api.file_storage.google_cloud_bucket_storage import GoogleCloudBucketStorage

class FileStorageFactory:

    @staticmethod
    def create():
        #TODO: Aqui se puede elegir que tipo de storage usar
        return GoogleCloudBucketStorage()
        #return FileSystemStorage()
