from django.urls import include, path, re_path
from django.contrib import admin
from finity_techserv_portfolio_website_app import views

app_name = 'finity_techserv_portfolio_website_app'

urlpatterns = [
    #Index url
    path('index/',views.index,name='index'),

    #AboutUS url
    path('aboutus/',views.aboutus,name='aboutus'),

    #Services url
    path('services/',views.services,name='services'),

    #contact url
    path('contact/',views.ContactForm,name='contact'),

    #contact url
    path('contactsubmit/',views.ContactSubmit,name='contactsubmit'),

    #signin url
    path('signin/',views.signin,name='signin'),

    #signup url
    path('signup/',views.signup,name='signup'),

    #submit url
    path('careersubmit/',views.careersubmit,name='careersubmit'),

    #submit url
    path('career/',views.careerform,name='career'),


    
]
