import datetime
from django.conf import settings
import os
from django.http import HttpResponse, Http404
from google.cloud import storage
from sistema_fcc_api.data_utils import DataUtils

class GoogleCloudBucketStorage():

    def delete_file(self, file_name, bucket_name=None):
        if not bucket_name:
            if settings.GOOGLE_CLOUD_BUCKET:
                bucket_name = settings.GOOGLE_CLOUD_BUCKET
            else:
                return {}

        client = storage.Client()
        bucket = client.bucket(bucket_name)
        blob = bucket.blob(file_name)
        blob.delete()

        return True

    def save_file(self, file_object, file_name, container_folder=None, prefix_folder=None, bucket_name=None,):


        if not bucket_name:
            if settings.GOOGLE_CLOUD_BUCKET:
                bucket_name = settings.GOOGLE_CLOUD_BUCKET
            else:
                return {}


        content_type = DataUtils.get_file_mimetype(file_name)

        if container_folder:
            file_name = container_folder+"/"+file_name

        if prefix_folder:
            file_name = prefix_folder + "/" + file_name

        file_stream = file_object.read()

        client = storage.Client()
        bucket = client.bucket(bucket_name)
        blob = bucket.blob(file_name)

        blob.upload_from_string(
            file_stream,
            content_type=content_type)

        url = blob.public_url

        return {"public_url": url}
