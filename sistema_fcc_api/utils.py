import random
import string
import base64

class Utils:

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
    def requestRawFileToB64(file):
        file_b64 = str(base64.b64encode(file.read()).decode())
        return file_b64

    @staticmethod
    def mimeFromFilename(filename):
        content_type = ""
        if '.mp4' in filename:
            content_type = "video/mp4"
        elif '.m4v' in filename:
            content_type = "video/mp4"
        else:
            content_type = "application/octet-stream"
        
        return content_type

    @staticmethod
    def requestFileToB64(logo):

        content_type = ""
        if '.jpg' in logo.name or '.jpeg' in logo.name:
            content_type = "data:image/jpeg;base64,"
        elif '.png' in logo.name:
            content_type = "data:image/png;base64,"

        logo_b64 = content_type+str(base64.b64encode(logo.read()).decode())

        return logo_b64