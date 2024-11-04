
from django.shortcuts import render, redirect,get_object_or_404,HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate,logout
from.models import UserProfile
from.models import book
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm,DataForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.http import JsonResponse
from django.db.models import Q


# Create your views here.




def books_media_gird_view_v2(request):
    
    books=book.objects.all().order_by('-id')
    return render(request,'books-media-gird-view-v2.html',{'books':books})


def books_media_detail_v1(request):
    
    books=book.objects.all()
    

    return render(request,'books-media-detail-v1.html',{'books':books})

def books_media_detail_v2(request):
    
    books=book.objects.all()
    

    return render(request,'books-media-detail-v2.html',{'books':books})



def cart(request,id):
    instance=get_object_or_404(book,id=id)
    if instance:
          data_value=book.objects.filter(id=id).get()
    else:
        data_value=""

    return render(request,'books-media-detail-v1.html',{'data':data_value,'instance':instance})
def checkout(request,id):
    form=DataForm()
    instance=get_object_or_404(book,id=id)
    if instance:
          datas=book.objects.filter(id=id).get()
    else:
        datas=None
    return render(request,'checkout.html',{'datas':datas,'form':form})
def order(request):
    return render(request,'order.html')
def contact(request):
    return render(request,'contact.html')
def services(request):
    return render(request,'services.html')
def cart1(request):
    return render(request,'cart.html')
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)       
        if form.is_valid():
            birth_date = form.cleaned_data['birth_date']
            phone_number = form.cleaned_data['phone_number']
            user = form.save()
            UserProfile.objects.create(user=user, birth_date=birth_date, phone_number=phone_number)
            login(request, user)
            msg="Signup completed"
            return render(request, 'signup.html', {'form': form,'msg':msg})
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'signup.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            request.session['username']=username
            if user is not None:
                login(request, user)
                return redirect(index)  # Redirect to the home page after successful login
        else:
            return render(request, 'signin.html', {'form': form})

    else:
        form = AuthenticationForm()

    return render(request, 'signin.html', {'form': form})



def signout(request):
    if 'username' in request.session:
        del request.session['username']
        
    logout(request)
    return redirect('signin')

def index(request):
      if request.user.is_authenticated:
        
         return render(request,'index.html')
      else:
            return redirect('signin')
@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            form.save()
            return redirect(index)
    else:
            form=PasswordChangeForm(request.user)
            return render(request, 'changepass.html',{'form':form})

# def description(request,id):
#     instance=get_object_or_404(book,id=id)
#     if instance:
#           data_value=book.objects.filter(id=id).get()
#     else:
#         data_value=""

#     return render(request,'cart.html',{'data':data_value,'instance':instance})


def search(request):
    query = request.GET.get('q') 
    if query:
        keywords = query.split()
        q_objects = Q()
        for keyword in keywords:
            q_objects |= (
                Q(title__icontains=keyword) |
                Q(author__icontains=keyword) |
                Q(description__icontains=keyword) 
                
            )
        books = book.objects.filter(q_objects)

        context = {
            'query': query,
            'books': books,
        }
        return render(request,'books-media-gird-view-v2.html',context)
    else:
        
        books=book.objects.all()
        
        return render(request,"search.html",{"books":books})