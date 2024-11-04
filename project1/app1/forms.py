from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile,data
from django.contrib.auth.models import User



class CustomUserCreationForm(UserCreationForm):
    birth_date= forms.DateField(widget=forms.DateInput(attrs={'type':'date','class':'forms-control'}))
    phone_number=forms.CharField(max_length=20)


    class Meta(UserCreationForm.Meta):
        model=User
  





class DataForm(forms.ModelForm):
    class Meta:
        model=data
        fields=['user','phone_number','Email','pincode','address','place','Paymentmethod']
        widgets={
            'user':forms.TextInput(attrs={'class':'form-control'}),
            'phone_number':forms.NumberInput(attrs={'class':'form-control'}),
            'Email':forms.EmailInput(attrs={'class':'form-control'}),
            'pincode':forms.NumberInput(attrs={'class':'form-control'}),
            'address':forms.Textarea(attrs={'class':'form-control'}),
            'place':forms.TextInput(attrs={'class':'form-control'}),
            
            'Paymentmethod':forms.RadioSelect(choices=data.Paymentmethod_CHOICES),
            
        }
