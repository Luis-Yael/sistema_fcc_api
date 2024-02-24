from sistema_fcc_api.models import *
import json
import requests
import datetime
import random
import string

class DataUtils:

    @staticmethod
    def generate_frontend_enc_key():
        key_1 = DataUtils.randomNumber(4)
        key_2 = DataUtils.randomNumber(4)
        key_3 = DataUtils.randomNumber(4)
        key_4 = DataUtils.randomNumber(4)

        key = []
        key.append(key_1)
        key.append(key_2)
        key.append(key_3)
        key.append(key_4)
        str_key = ",".join(key)

        return str_key

    @staticmethod
    def randomString(stringLength=10):
        """Generate a random string of fixed length """
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(stringLength))

    @staticmethod
    def randomNumber(numberLength=10):
        """Generate a random number of fixed length """
        digits = string.digits
        return ''.join(random.choice(digits) for i in range(numberLength))

    @staticmethod
    def get_file_extension(mime_type):
        if mime_type:
            if mime_type=="video/mp4":
                return ".mp4"
            elif mime_type=="video/x-m4v":
                return ".m4v"
            elif mime_type=="video/webm":
                return ".webm"
        else:
            return ""

    @staticmethod
    def get_file_mimetype(file_name):
        if file_name:
            if ".mp4" in file_name:
                return "video/mp4"
            elif ".m4v" in file_name:
                return "video/x-m4v"
            elif ".webm" in file_name:
                return "video/webm"
        else:
            return ""


    @staticmethod
    def is_url(text):
        return text.startswith('http://') or text.startswith('https://')

    @staticmethod
    def is_url_image(image_url):
        image_formats = ("image/png", "image/jpeg", "image/jpg")
        r = requests.head(image_url)
        print("Content type:: "+str(r.headers["content-type"]))
        if r.headers["content-type"] in image_formats:
            return True
        return False

    @staticmethod
    def getUrl(request):

        absolute_uri = request.build_absolute_uri()
        full_path = request.get_full_path()

        url = absolute_uri
        cut = absolute_uri.find(full_path)
        if cut > 0:
            url = absolute_uri.replace(full_path,"")

        return url
