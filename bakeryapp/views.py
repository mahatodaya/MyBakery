from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
# from operator import attrgetter
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def index(request):
    # context = {
    #     'items': Item.objects.all()
    # }  ,context
    
    return render(request,"index.html")   

def about(request):
    return render(request, 'about.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['user']
        password = request.POST['psw']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            messages.info(request,'Login Sucessfull')
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')

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
            if User.objects.filter(username=username).exists():
                messages.info(request,'This username was already registered!')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'This email was already registered!')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, password=password, email=email,first_name=first_name,last_name=last_name)
                auth.login(request, user)
                user.save()
                print('User created')
                return redirect('login')
        else:
            messages.info(request,'Invalid Password')
            return redirect('signup')
        return redirect('/')
    else:
        return render(request,'signup.html')
    







#     def login(request):
# if request.user.is_authenticated():
    #     return redirect('index')
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']

#         user = auth.authenticate(username=username,password=password)

#         if user is not None:
#             auth.login(request, user)
#             return redirect('/')

#         else:
#             messages.info(request,'invalid credentials')
#             return redirect('login')
#     else:
#         return render(request,'login.html')

# def register(request):

#     if request.method == 'POST':
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         username = request.POST['username']
#         password1 = request.POST['password1']
#         password2 = request.POST['password2']
#         email = request.POST['email']

#         if(password1==password2):
#             if User.objects.filter(username=username).exists():
#                 messages.info(request,'Username is used already')
#                 return redirect('register')
#             elif User.objects.filter(email=email).exists():
#                 messages.info(request,'Email is used already')
#                 return redirect('register')
#             else:
#                 user = User.objects.create_user(username=username, password=password1, email=email,first_name=first_name,last_name=last_name)
#                 user.save();
#                 print('User created')
#                 return redirect('login')

#         else:
#             messages.info(request,'Invalid')
#             return redirect('register')
#         return redirect('/')

#     else:
#         return render(request,'register.html')





def store(request):

    # page = request.GET.get('page',1)


    return render(request, 'store.html')

def menu(request):
    return render(request, 'menu.html')

def contact(request):
    return render(request, 'contact.html')

def items(request):
    user_list=User.objects.all()
    paginator = Paginator(user_list, 4) # Show 4 items per page.
    page = request.GET.get('page')
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    
    return render(request, 'items.html',{'users': users})
    # if ".pagination" in request.POST:

    #     users = User.objects.raw("select * from auth_user limit 4 offset 8")
    # else:
    #     users = User.objects.raw("select * from auth_user limit 4 offset 0")
    # return render(request, 'items.html', {'users': users})

    #pager start
    # page = request.GET.get('page', 1)
    # paginator = Paginator(books, 9)
    # try:
    #     users = paginator.page(page)
    # except PageNotAnInteger:
    #     users = paginator.page(1)
    # except EmptyPage:
    #     users = paginator.page(paginator.num_pages)
    #pager end


def delete(request,id):
    users = User.objects.get(id=id)
    users.delete()
    return redirect('items')
    # messages.info(request,'Invalid Password')

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