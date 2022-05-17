from django.urls import path
from .views import SignUpView, user_logout, login_user, register_user
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('password_change/', PasswordChangeView.as_view(template_name='registration/password_change.html'), name='password_change'),
    path('password_change_done/', PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), name='password_change_done'),

    #api urls
    path('api-register/', register_user, name='api-user-register'),
    path('api-login/', login_user, name='api-user-login'),
    path('api-logout/', user_logout, name='api-user-logout'),
]