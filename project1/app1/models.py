from django.db import models
class UserProfile(models.Model):
    user=models.OneToOneField('auth.user',on_delete=models.CASCADE)
    birth_date=models.DateField()
    phone_number=models.CharField(max_length=20)
class book(models.Model):
    
    title=models.CharField(max_length=60,unique=True)
    author=models.CharField(max_length=20,unique=True)
    bookid=models.IntegerField()
    price=models.IntegerField()
    availablecopies=models.IntegerField()
    description=models.TextField()
    
    image=models.ImageField(upload_to='image',default="")


class data(models.Model):
    Paymentmethod_CHOICES=[
       ('c','cash on delivery'),
       ('g','gpay'),
       

   ]
    

    user = models.OneToOneField('auth.user', on_delete=models.CASCADE)
    phone_number=models.CharField(max_length=20)
    Email=models.EmailField(max_length=20)
    pincode=models.IntegerField()
    address=models.TextField()
    place=models.CharField(max_length=50)
    Paymentmethod=models.CharField(max_length=1,choices=Paymentmethod_CHOICES)

   




# Create your models here.
