from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegistrationForm, ProductForm
from django.http import HttpResponse
from django.contrib.auth.forms import  UserCreationForm

# Create your views here.
def home(request):
    products = Product.objects.all()


    context = {'products':products}
    return render(request, 'base/home.html', context)


def view(request, pk):
    item = Product.objects.get(id=pk)
    context = {'item': item }
    return render(request, 'base/view.html', context)




def add(request):
    form = ProductForm()
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            product = form.save(commit=False)
            product.seller = request.user
            product.save()
            return redirect('view', pk=product.id)
    return render(request, 'base/add.html',{'form':form})





def edit(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)

        if form.is_valid():
            form.save()
            return redirect('view', pk=product.id)
    return render(request, 'base/add.html',{'form':form})




def delete(request, pk):
    product = Product.objects.get(id=pk)

    if request.method == 'POST':
        product.delete()
        return redirect('home')
        
    return render(request, 'base/delete.html', {'product':product})



def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')

    form = LoginForm()


    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        
        else:
            return HttpResponse('Username or Password does not exist ')

    return render(request, 'base/login.html', {'form':form})




def register(request):
    form = RegistrationForm()


    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
        login(request, user)

        return redirect('home')
    return render(request, 'base/register.html', {'form':form})



def logoutUser(request):
    logout(request)
    return redirect('home')