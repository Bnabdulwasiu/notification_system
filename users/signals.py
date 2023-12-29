from django.core.mail import send_mail
from .models import CustomUser
from django.conf import settings
from django.dispatch import receiver
from axes.signals import user_locked_out

@receiver(user_locked_out)
def handle_brute_force_attack(sender, request, **kwargs):
    
    admin_users = CustomUser.objects.filter(is_admin=True, is_superuser=True)
    
    subject = "Brute Force Attack Detected"
    message = 'A brute foce attack has been detected in your django app,\
        Please take necessary actions.'
        
    for admin_user in admin_users:
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [admin_user.email])
    