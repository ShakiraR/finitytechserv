from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth import login, logout, authenticate
from finity_techserv_portfolio_website_app.models import CustomUser,Contact,Career,Quotation
from django.contrib.auth.hashers import make_password
from django.core.files.storage import FileSystemStorage


# Create your views here.
#index view
def index(request):
    data = { }
    return render(request, 'finity_techserv_portfolio_website_app/index.html', data)

#AboutUs view
def aboutus(request):
    data = { }
    return render(request, 'finity_techserv_portfolio_website_app/aboutus.html', data) 

#Services view
def services(request):
    data = { }
    return render(request, 'finity_techserv_portfolio_website_app/services.html', data) 

def ContactForm(request):
    data = { }
    return render(request, 'finity_techserv_portfolio_website_app/contact.html', data)     

  
#contact view
def ContactSubmit(request):
    if request.method == "POST":
        FirstName = request.POST['fname']
        LastName = request.POST['lname']
        PhoneNo = request.POST['phone']
        Email = request.POST['email']
        Message = request.POST['message']
        Contact.objects.create(FirstName = FirstName,
                                LastName = LastName,
                                PhoneNo = PhoneNo,
                                Email = Email,
                                Message = Message)
        return HttpResponseRedirect(reverse('finity_techserv_portfolio_website_app:contact'))                                        

     

#signin view
def signin(request):
    if request.method == "POST":
        email =  request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'finity_techserv_portfolio_website_app/services.html')   
        else:
            return render(request, 'finity_techserv_portfolio_website_app/signin.html',{'error_message': 'Username or Password Incorrect!'})

    else:
        return render(request, 'finity_techserv_portfolio_website_app/signin.html')

#signup view
def signup(request):
    if request.method == "POST":
        email =  request.POST['email']
        password = request.POST['password']
        # confirm_password = request.POST['confirm_password']
        # if password != confirm_password:
        #     return render(request, 'finity_techserv_portfolio_website_app/signup.html',{'error_message':'Passwords do not match!'})
        if CustomUser.objects.filter(username = email).exists():
            return render(request, 'finity_techserv_portfolio_website_app/signup.html',{'error_message':'Username already exists!'})
        else:
            # Role 2 is for admin, 1 is for super admin.
            user = CustomUser.objects.create(username=email, password= make_password(password), user_role=2)
            login(request, user)
            return render(request, 'finity_techserv_portfolio_website_app/signin.html') 
    else:
        return render(request, 'finity_techserv_portfolio_website_app/signup.html')
 

#submit view
def submit(request):
    data = { }
    return render(request, 'finity_techserv_portfolio_website_app/submit.html', data) 

#submit view
def careerform(request):
    data = { }
    return render(request, 'finity_techserv_portfolio_website_app/career.html', data)


def careersubmit(request):
    if request.method == "POST":
        Name = request.POST['name']
        Email = request.POST['email']
        PhoneNo = request.POST['phone']
        Message = request.POST['message']
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)

        Career.objects.create(Name = Name,
                               Email = Email,
                               PhoneNo = PhoneNo,
                               Resume = myfile,
                               Message = Message)
        return HttpResponseRedirect(reverse('finity_techserv_portfolio_website_app:career'))                              


def Quotationform(request):
    data = { }
    return render(request, 'finity_techserv_portfolio_website_app/aboutus.html', data)
    
def Quotationsubmit(request):
    if request.method == "POST":
        Name = request.POST['name']
        Email = request.POST['email']
        PhoneNo = request.POST['phone']
        BusinessSector = request.POST['BusinessSector']
        Message = request.POST['message']
        Quotation.objects.create(Name = Name,
                               Email = Email,
                               PhoneNo = PhoneNo,
                               BusinessSector = BusinessSector,
                               Message = Message)
        return HttpResponseRedirect(reverse('finity_techserv_portfolio_website_app:Quotation'))

def QuotationIndexform(request):
    data = { }
    return render(request, 'finity_techserv_portfolio_website_app/index.html', data)
    
def QuotationIndexsubmit(request):
    if request.method == "POST":
        Name = request.POST['name']
        Email = request.POST['email']
        PhoneNo = request.POST['phone']
        BusinessSector = request.POST['BusinessSector']
        Message = request.POST['message']
        Quotation.objects.create(Name = Name,
                               Email = Email,
                               PhoneNo = PhoneNo,
                               BusinessSector = BusinessSector,
                               Message = Message)
        return HttpResponseRedirect(reverse('finity_techserv_portfolio_website_app:QuotationIndex'))                                      
