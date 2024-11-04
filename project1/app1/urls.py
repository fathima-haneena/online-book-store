from django.urls import path,include
from . import views
urlpatterns = [
   
     path('',views.index,name='index'),
     path('books-media-detail-v1/',views.books_media_detail_v1,name='books_media_detail_v1'),
     path('books-media-detail-v2/',views.books_media_detail_v2,name='books_media_detail_v2'),
     path('books-media-gird-view-v2/',views.books_media_gird_view_v2,name='books_media_gird_view_v2'),
     path('cart/<int:id>/',views.cart,name='cart'),
     path('checkout/<int:id>/',views.checkout,name='checkout'),
     path('contact.html',views.contact,name='contact'),
     path('services.html',views.services,name='services'),
     path('signin',views.signin,name='signin'),
     path('signup',views.signup,name='signup'),
     path('signout',views.signout,name='signout'),
     path('changepass.html',views.change_password,name='change_password'),
     path('order', views.order, name="order"),
     path('cart', views.cart1, name="cart1"),
     path('search/',views.search,name='search'),
    

]
