from django.urls import path
from . import views

app_name = 'user_login'

urlpatterns = [

    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register/password', views.register_pass, name='register_password'),
    path('login/', views.user_login, name='login'),

    path('register', views.Register.as_view(), name='register'),
    path('check_otp', views.CheckOtpView.as_view(), name='verification'),
    path('profile', views.ProfileView.as_view(), name='profile'),
    path('address_profile', views.AddressProfile.as_view(), name='address_profile'),
    path('message_profile', views.ProfileMessage.as_view(), name='message_profile'),
    path('order_profile', views.ProfileOrderUserView.as_view(), name='order_profile'),
    path('personal_profile', views.ProfilePersonalView.as_view(), name='personal_profile'),


]
