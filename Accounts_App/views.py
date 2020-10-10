from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def Accounts_Register_View(request, *args, **kwargs):

    if request.method == 'POST':
        FirstName = request.POST['firstname']
        LastName = request.POST['lastname']
        UserName = request.POST['username']
        Email = request.POST['emailid']
        Password = request.POST['password']
        ConfirmPassword = request.POST['confirmpassword']  

        if Password == ConfirmPassword:
            if User.objects.filter(username=UserName).exists(): 
                messages.info(request, "Username is not available. Try another") 
                return redirect('/accounts/Register/')
            elif User.objects.filter(email=Email).exists():
                messages.info(request,"Email is already exists in the database")
                return redirect('/accounts/Register/') 
            else:
                New_User = User.objects.create_user(username=UserName, first_name=FirstName, last_name=LastName, password=Password, email=Email)
                New_User.save()
                return redirect('/accounts/Login/')
        else:
            messages.info(request,"Passwords are not matching.")
            return redirect('/accounts/Register/')
    else:
        return render(request, 'Accounts_Register.html')

def Accounts_Login_View(request):
    if request.method == 'POST':
        UserName = request.POST['username']
        Password = request.POST['password']

        user = auth.authenticate(username=UserName, password=Password)

        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect('/')
        else:
            messages.info(request, "Please enter valid credentials.")
            return redirect('/accounts/Login/')
    else:
        return render(request, 'Accounts_Login.html')

def Accounts_Logout_View(request):
    auth.logout(request)
    return redirect('Login_Page')