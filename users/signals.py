# from django.core.mail import send_mail
from .models import CustomUser
from django.conf import settings
from django.dispatch import receiver
from axes.signals import user_locked_out
import yagmail
from yagmail import YagConnectionClosed
import socket

@receiver(user_locked_out)
def handle_brute_force_attack(sender, request, **kwargs):
    
    admin_users = [user.email for user \
                   in CustomUser.objects.filter(is_admin=True) ]                 
    
    subject = "Illegal Login Attempt In your Data App"
    message = 'A brute foce attack has been detected in your Data App,\
        Please take necessary actions.'
    email_sender = 'abuumair.dev@gmail.com'
    email_password = 'qjipdmifnjddfvbk'
    headers = {
        "From": "Data App Notification\
            <abuumair.dev@gmail.com>"
    }
    
    try:
        yag = yagmail.SMTP(email_sender, email_password)
        contents = [message]
        yag.send(admin_users, subject, contents, headers=headers)
        
    except socket.error:
        print('Connection error')

