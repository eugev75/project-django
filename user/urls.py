from django.urls import path
from user import views
from django.contrib.auth.views import LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('add/', views.SignUpView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('edit/', views.UserUpdateView.as_view(), name='edit_user'),
    path('delete', views.UserDeleteView.as_view(), name='delete_user'),
    path('password/', views.PasswordsChangeView.as_view(), name='change_password'),
    path('profile/<int:pk>', views.ViewProfile.as_view(), name='view_profile'),

    path('password_reset/', PasswordResetView.as_view(
        template_name='password/password_reset.html'
    ), name='password_reset'),

    path('password_reset/done/', PasswordResetDoneView.as_view(
        template_name='password/password_reset_done.html'
    ), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name='password/password_reset_confirm.html'
    ), name='password_reset_confirm'),

    path('reset/done/', PasswordResetCompleteView.as_view(
        template_name='password/password_reset_complete.html'
    ), name='password_reset_complete'),
]
