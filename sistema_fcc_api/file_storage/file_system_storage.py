import datetime
from django.conf import settings
import os
from django.http import HttpResponse, Http404

class FileSystemStorage():

    def save_file(self, file_stream, file_name):
        #TODO: Yet to implement...
        return None