from celery import shared_task
from django.core.mail import EmailMessage
import logging

@shared_task
def send_email_task(subject, body, reciever):
    email = EmailMessage(subject, body, to=reciever)
    email.send()
