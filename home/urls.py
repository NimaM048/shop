from django.urls import path
from . import views



app_name = 'home'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('contact_us', views.ContactUsView.as_view(), name='contactus'),
    path('about_us', views.AboutUsView.as_view(), name='aboutus'),
    path('qs', views.QSView.as_view(), name='qs'),

    path('rules', views.RulesView.as_view(), name='rules'),


]