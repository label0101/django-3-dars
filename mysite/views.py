from django.shortcuts import render

# Create your views here.

def home_view(requst):
    return render(request=requst,template_name='index.html')

def service_view(requst):
    return render(request=requst,template_name='service.html')

def portfolio_view(requst):
    return render(request=requst,template_name='portfolio.html')

def about_view(requst):
    return render(request=requst,template_name='about.html')

def contact_view(requst):
    return render(request=requst,template_name='contact.html')
