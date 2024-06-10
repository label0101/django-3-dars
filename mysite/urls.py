from django.urls import path
from .views import home_view,service_view,portfolio_view,about_view,contact_view

urlpatterns = [
    path('',home_view,name='home-page'),
    path('service/',service_view,name='service-page'),
    path('portfolio/',portfolio_view,name='portfolio-page'),
    path('about/',about_view,name='about-page'),
    path('contact/',contact_view,name='contact-page'),
]