from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate,logout
from.models import UserProfile,JobListing
from django.shortcuts import render, redirect,get_object_or_404
from .forms import CustomUserCreationForm,JobListingForm,ContactForm,JobApplyForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views import View
from django.views.generic import ListView
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    qs = JobListing.objects.all()
    jobs = JobListing.objects.all().count()
    user = User.objects.all().count()
    company_name = JobListing.objects.filter(company_name__startswith='').count()
    paginator = Paginator(qs, 5)  # Show 5 jobs per page
    page = request.GET.get('page')
    try:
        qs = paginator.page(page)
    except PageNotAnInteger:
        qs = paginator.page(1)
    except EmptyPage:
        qs = paginator.page(paginator.num_pages)

    context = {
        'query': qs,
        'job_qs': jobs,
        'company_name': company_name,
        'candidates': user
    }
    return render(request, "index.html", context)

   
   
def about(request):
    return render(request,'about.html')

def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        instance = form.save()
        instance.save()
        return redirect('index')
    context = {
        'form': form
    }
    return render(request, "contact.html", context)

        


    


def job_listing(request):
    query = JobListing.objects.all().count()

    qs = JobListing.objects.all().order_by('-published_on')
    paginator = Paginator(qs, 3)  # Show 3 jobs per page
    page = request.GET.get('page')
    try:
        qs = paginator.page(page)
    except PageNotAnInteger:
        qs = paginator.page(1)
    except EmptyPage:
        qs = paginator.page(paginator.num_pages)

    context = {
        'query': qs,
        'job_qs': query

    }
    return render(request, "job-listings.html", context)

    
    
    
    
def job_single(request,id):
  if request.user.is_authenticated:
#   if 'username' in request.session:
    instance=get_object_or_404(JobListing,id=id)
    if instance:
          data_value=JobListing.objects.filter(id=id).get()
    else:
        data_value=""
    return render(request,'job-single.html',{'data':data_value,'instance':instance})
  else:
    return redirect('signin')
  
    
  
@login_required
def post_job(request):
    form = JobListingForm(request.POST or None)
    if form.is_valid():
        instance = form.save()
        instance.save()
        return redirect('job_listing')
    context = {
        'form': form,

    }
    return render(request, "post-job.html", context)
   



def service(request):
    return render(request,'services.html')

@login_required
def apply_job(request):
    form = JobApplyForm(request.POST or None, request.FILES)
    if form.is_valid():
        instance = form.save()
        instance.save()
        return redirect('index')
    context = {
        'form': form,

    }
    return render(request, "job_apply.html", context)
# def apply_job(request):
    
#         form=JobApplyForm(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()
#             form=JobApplyForm()
#             return render(request,'job_apply.html',{'form':form})
#         else:
#             return render(request,'job_apply.html',{'form':form})
        
    
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)       
        if form.is_valid():
            birth_date = form.cleaned_data['birth_date']
            phone_number = form.cleaned_data['phone_number']
            user = form.save()
            UserProfile.objects.create(user=user, birth_date=birth_date, phone_number=phone_number)
            login(request, user)
            msg="Signup completed"
            return render(request, 'register.html', {'form': form,'msg':msg})
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'register.html', {'form': form})

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
                return redirect('/')  # Redirect to the home page after successful login
        else:
            return render(request, 'signin.html', {'form': form})

    else:
        form = AuthenticationForm()

    return render(request, 'signin.html', {'form': form})



def signout(request):
    if 'username' in request.session:
        del request.session['username']
        
    logout(request)
    return redirect('index')


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

class SearchView(ListView):
    model = JobListing
    template_name = 'search.html'
    context_object_name = 'jobs'

    def get_queryset(self):
        return self.model.objects.filter(title__contains=self.request.GET['title'],
                                         job_location__contains=self.request.GET['job_location'],
                                         employment_status__contains=self.request.GET['employment_status'])
