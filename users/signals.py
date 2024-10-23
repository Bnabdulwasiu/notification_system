from .models import CustomUser
from django.contrib.auth import get_user_model
from django.conf import settings
from django.dispatch import receiver
from axes.signals import user_locked_out
import yagmail
from yagmail import YagConnectionClosed
import socket
from .tasks import send_email_task

CustomUser = get_user_model()

@receiver(user_locked_out)
def handle_brute_force_attack(sender, request, **kwargs):
    
    admin_users = [user.email for user 
                in CustomUser.objects.filter(is_admin=True)]
    
    subject = "Illegal Login Attempt In your Data App"
    contents = f'A BRUTE FORCE attack has been detected in your Data App,\n\
            \nCopy this link to your browser to reset your password: \n<a>{request.META.get("HTTP_HOST")}/users/password_reset</a> '
    try:
        for user in admin_users:
            send_email_task.delay(subject, contents, user)
        # print("Email sent")
    except Exception as e:
        print(f"Could not send email due to {e}")
