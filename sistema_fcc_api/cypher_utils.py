import base64
from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from django.conf import settings

class CypherUtils:

    @staticmethod
    def encripta(plaintext):
        password = settings.CRYPTO_PASSWORD
        enc_bytes =  CypherUtils.encrypt1(plaintext.encode('utf-8'), password.encode('utf-8'))
        return enc_bytes.decode('utf-8')

    @staticmethod
    def desencripta(cyphertext):
        password = settings.CRYPTO_PASSWORD
        denc_bytes =  CypherUtils.decrypt1(cyphertext.encode('utf-8'), password.encode('utf-8'))
        return denc_bytes.decode('utf-8')

    @staticmethod
    def cipherFernet(password):
        key = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=b'hdjk', iterations=1000, backend=default_backend()).derive(password)
        return Fernet(base64.urlsafe_b64encode(key))

    @staticmethod
    def encrypt1(plaintext, password):
        return CypherUtils.cipherFernet(password).encrypt(plaintext)

    @staticmethod
    def decrypt1(ciphertext, password):
        return CypherUtils.cipherFernet(password).decrypt(ciphertext)