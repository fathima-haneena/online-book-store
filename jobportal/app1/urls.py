from django.urls import path
from . import views

from .views import *
urlpatterns = [
    path('register/',views.register,name='register'),
    path('signin/',views.signin,name='signin'),
    path('signout/',views.signout,name='signout'),
    path('',views.index,name='index'),
    path('change_password/',views.change_password,name='change_password'),
    path('about/',views.about,name='about'),
   
    path('contact/',views.contact,name='contact'),
    
    path('job_list/',views.job_listing,name='job_listing'),
    path('job_single/<int:id>/',views.job_single,name='job_single'),
    
   
    path('post_job/',views.post_job,name='post_job'),
    
    path('service/',views.service,name='service'),
    
    path('apply/', views.apply_job, name='apply'),
    
    path('search',SearchView.as_view(),name='search'),
    

]