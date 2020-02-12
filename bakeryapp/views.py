from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Products
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from .forms import ProductForm

# Create your views here.
def index(request):
    return render(request,"index.html")   

def about(request):
    return render(request, 'about.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['user']
        password = request.POST['psw']

        # check username and password from database
        user = auth.authenticate(username=username,password=password)


        if user is not None:
            auth.login(request, user)
            messages.info(request,'Login Sucessfull')
            return redirect('/')
        else:
            messages.info(request,'Invalid Login')
    return redirect('/')
 
def logout(request):
    auth.logout(request)
    return redirect('/')

def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']
        if(password == confirmpassword):

            # Validation for existing users
            if User.objects.filter(username=username).exists():
                messages.info(request,'This username was already registered!')
                return redirect('/')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'This email was already registered!')
                return redirect('/')
            else:
                user = User.objects.create_user(username=username, password=password, email=email,first_name=first_name,last_name=last_name)
                auth.login(request, user)
                user.save()
                return redirect('/')
        else:
            messages.info(request,'Invalid Password')
            return redirect('/')
        return redirect('/')
    else:
        return render(request,'/')
    
def store(request):

    prdts = Products.objects.all()
    return render(request, 'store.html', {'prdts': prdts})

def menu(request):
    return render(request, 'menu.html')

def contact(request):
    return render(request, 'contact.html')

def admindashboard(request):
    user_list=User.objects.all()
    
    # pagination for all users
    paginator = Paginator(user_list, 4) # Show 4 items per page.
    page = request.GET.get('page')
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    product_list=Products.objects.all()

    # pagination for all available products
    paginator = Paginator(product_list, 4) # Show 4 items per page.
    page = request.GET.get('page')
    try:
        product_list = paginator.page(page)
    except PageNotAnInteger:
        product_list = paginator.page(1)
    except EmptyPage:
        product_list = paginator.page(paginator.num_pages)

    return render(request, 'admindashboard.html',{'users': users, 'product_list':product_list})

def delete(request,id):
    users = User.objects.get(id=id)
    users.delete()
    return redirect('items')

def edit(request, id):
    users = User.objects.get(id=id)
    if request.method == 'POST':
        users.first_name = request.POST['first_name']
        users.last_name = request.POST['last_name']
        users.username = request.POST['username']
        users.email = request.POST['email']
        users.password = request.POST['password']
        users.save()
        return redirect('/')  

    return render(request, 'edit.html', {'users' : users})

def search(request):
    if request.method == 'POST':
        users = User.objects.filter(username__icontains = request.POST['searchTerm']).values()
        print(request.POST['searchTerm'])
        return JsonResponse(list(users), safe=False)

def search_products(request):
    if request.method == 'POST':
        product = Products.objects.filter(name__icontains = request.POST['searchTerm']).values()
        print(request.POST['searchTerm'])
        return JsonResponse(list(product), safe=False)

def create_products(request):
    form = ProductForm()
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request, 'Inserted')
    return render(request, 'create.html', context)

def update_products(request, id):
    product = Products.objects.get(id = id)
    form = ProductForm(instance = product)
    context = {
        'form': form
    }
    if request.method == 'POST':
        product = Products.objects.get(id = id)
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.info(request, 'Updated')
            return redirect('admindashboard')
    return render(request, 'create.html', context)
        
def delete_products(request, id):
    product = Products.objects.get(id = id)
    product.delete()
    return redirect('admindashboard')
        
