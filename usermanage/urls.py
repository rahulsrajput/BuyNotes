from django.urls import path, include
from usermanage import views
urlpatterns = [
    path('login/', views.loginUser, name='loginUser'),
    path('logout/', views.logoutUser, name='logoutUser'),
    path('register/', views.registerUser, name='registerUser'),
    path('password-reset/', views.PasswordReset.as_view(), name='passwordReset'),
    path('password-reset-done/', views.PasswordResetDone.as_view(), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>', views.PasswordResetConfirm.as_view(), name='password_reset_confirm'),
    path('password-reset-complete/', views.PasswordResetComplete.as_view(), name='password_reset_complete'),
    path('password-change/',views.PasswordChange.as_view(), name='passwordChange'),
    path('password-change-done/', views.PasswordChangeDone.as_view(), name='password_change_done')
]