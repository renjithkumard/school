from django.contrib import messages, auth
from django.shortcuts import render, redirect


# Create your views here.
def home(request):
    return render(request, 'index.html')
def form(request):
    return render(request, 'form.html')
def signup(request):

    if request.method == 'POST':
        username = request.POST['user']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('for')

        else:
            messages.info(request, "invalid credential")
            return redirect('sign')

    return render(request,'signup.html' )

def page(request):

    return render(request, 'page.html')

def about(request):

    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def courses(request):
    return render(request, 'courses.html')


