from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import OrderForm, SizeForm, CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Count, F

# Create your views here.


@login_required(login_url='login')
def home(request):
    products_pizza = Product.objects.all()
    products = []
    order    = Order.objects.get(pk=request.session['order'])
    order_products = Order_product.objects.filter(orders=order)
    total_price = 0
    for item in order_products:
        total_price += item.quantity * Price.objects.get(size=item.size).price
    
    for product in products_pizza:
        products.append({'product': product, 'form':SizeForm(initial={'product':product})})
    
    context = {'products' : products, 
                'order': order,
                'order_products' : order_products,
                'products_pizza': products_pizza,
                'total_price': total_price
             
            }
                
        
    return render(request, 'dashboard.html', context)
        
    


    
    
@login_required(login_url='login')
def product(request, pk):
    product = Product.objects.get(id=pk)
    context = {'product': product}
    return render(request, 'product.html', context)


# def createOrder(request):
#     orders = Order.objects.all()
#     form = OrderForm()
#     if request.method == "POST":
#         form = OrderForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("/")
    
#     context = {'form':form}
#     return render(request, "order_form.html", context)


# def deleteOrder(request, pk):
#     product = Product.objects.get(id=pk)
#     if request.method == 'POST':
#         product.delete()
#         return redirect('/')
#     context ={'product':product}
#     return render(request, "delete_form.html", context)

# def updateOrder(request, pk):
#     products = Product.objects.get(id=pk)
#     form = OrderForm()
#     if request.method == "POST":
#         form = OrderForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("/")
#     context = {'form':form}
#     return render(request, "order_form.html", context)


@login_required(login_url='login')
def addtocart(request):
    order    = Order.objects.get(pk=request.session['order'])
    if request.method == 'POST':
        form = SizeForm(request.POST)
        if form.is_valid():
            order_product = form.save()
            order_product.orders = order
            order_product.save()
    return redirect ("/")
            



@login_required(login_url='login')    
def removefromcart(request, pk):
    cart_item = Order_product.objects.get(pk=pk)
    if cart_item.quantity == 1:
        cart_item.delete()
    else:
        cart_item.quantity -= 1
        cart_item.save()
    return redirect ("/")
    
   
@login_required(login_url='login')
def additemtocart (request, pk):
    cart_item = Order_product.objects.get(pk=pk)
    if cart_item.quantity > 0:
        cart_item.quantity += 1
        cart_item.save()
        
    return redirect ("/")



def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was creted for ' + user)
                return redirect('login')

        context = {'form': form}
        return render(request, 'register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect ('home')
            else:
                messages.info(request, 'Username OR password is incorrect')    

        context = {}
        return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')

