from celery import shared_task
from time import sleep

from django.core.mail import send_mail  
from .views import *



@shared_task
def send_mail_task(email):
    send_mail('Your account is activated', 'Thanks for registering.', 
    'utsabkumaragrawal@gmail.com',
    [email],
    fail_silently= False,
    )

    return None