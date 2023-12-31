from django.urls import path
from django.contrib.auth import views as auth_views

from .views import SignUpView, CustomLoginView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('password_reset/',
         auth_views.PasswordResetView.as_view(template_name='password_reset.html'),
                                        name='password_reset'),
    path('password_reset/done',
         auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
                                        name='password_reset_done')
    
]

