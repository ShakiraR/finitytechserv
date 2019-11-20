from django.shortcuts import render

# Create your views here.
#index view
def index(request):
    data = { }
    return render(request, 'finity_techserv_portfolio_website_app/index.html', data)

#AboutUs view
def aboutus(request):
    data = { }
    return render(request, 'finity_techserv_portfolio_website_app/about_us.html', data) 

#Services view
def services(request):
    data = { }
    return render(request, 'finity_techserv_portfolio_website_app/services.html', data) 

#Service_details view
def service_details(request):
    data = { }
    return render(request, 'finity_techserv_portfolio_website_app/service_details.html', data)    



#contact view
def contact(request):
    data = { }
    return render(request, 'finity_techserv_portfolio_website_app/contact.html', data) 

#signin view
def signin(request):
    data = { }
    return render(request, 'finity_techserv_portfolio_website_app/signin.html', data)

#signup view
def signup(request):
    data = { }
    return render(request, 'finity_techserv_portfolio_website_app/signup.html', data)  

#submit view
def submit(request):
    data = { }
    return render(request, 'finity_techserv_portfolio_website_app/submit.html', data)                    



    