from pyexpat.errors import messages
from django.shortcuts import render, redirect , HttpResponse
from finalproject.models import  finalproject
from finalproject.forms import  LoginForm
from django.contrib import messages
# Create your views here.



def is_logged_in(request):
    return 'username' in request.session

def home(request):
    if is_logged_in(request):
        return redirect('/post/home')
    
    else:
        return redirect('/finalproject/login')




def login(request):
    if request.method == 'GET':
        return render(request, 'login.html', context={'login_form': LoginForm})
    elif request.method == 'POST':
        #check if username and password are in request.POST
        form = LoginForm(request.POST)
        if not form.is_valid():
            
            redirect('/finalproject/login')
        
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        
        if not finalproject.objects.filter(username = username).exists():
            messages.error(request, 'wrong user password')
            return redirect('/finalproject/login')    
        user = finalproject.objects.get(username=username)
        #if user.password == password # this won't work because the password in the database is hashed.
        if not user.check_password(password):
           
            return redirect('/finalproject/login')
        
        request.session['username'] = username
        
        return redirect('/post/home')
    else:
        return HttpResponse("Method not allowed")

       



def test_login(request):
    if 'username' not in request.session:
        return HttpResponse("You are not logged in")
    else:
        return HttpResponse(f"You are logged in as {request.session['username']}")






def logout(request):
    if 'username' in request.session:
        del request.session['username']
    messages.info(request, "You are logged out")
    return redirect('/finalproject/logout')