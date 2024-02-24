from django.conf import settings
from django.http import HttpResponse, Http404
from django.core.mail import EmailMessage
from rest_framework import status
from rest_framework.response import Response
from django.core.mail import EmailMessage
import datetime
import os
import threading

class MailsBridge:

    @staticmethod 
    def send_mail_async(subject=None,reply_email=None, from_email=None,to_email=None,cc=None,bcc=None,html_message=None):

        if html_message:
            html_message = html_message.replace("á","&aacute;")
            html_message = html_message.replace("é","&eacute;")
            html_message = html_message.replace("í","&iacute;")
            html_message = html_message.replace("ó","&oacute;")
            html_message = html_message.replace("ú","&uacute;")
            html_message = html_message.replace("Á","&Aacute;")
            html_message = html_message.replace("É","&Eacute;")
            html_message = html_message.replace("Í","&Iacute;")
            html_message = html_message.replace("Ó","&Oacute;")
            html_message = html_message.replace("Ú","&Uacute;")

        send_thread = threading.Thread(target=MailsBridge.send_mail_sync, args=(subject, reply_email, from_email, to_email, cc, bcc, html_message))
        send_thread.start() 

    @staticmethod
    def send_mail_sync(subject=None,reply_email=None, from_email=None,to_email=None,cc=None,bcc=None,html_message_custom=None):

        headers = {}
        if reply_email!="":
            headers = {'Reply-To': reply_email}
            
        if cc:
            msg = EmailMessage(subject, html_message_custom, from_email, [to_email], bcc=[bcc], headers=headers, cc=[cc])
        else:
            msg = EmailMessage(subject, html_message_custom, from_email, [to_email], bcc=[bcc], headers=headers)
        msg.content_subtype = "html"
        res = msg.send()