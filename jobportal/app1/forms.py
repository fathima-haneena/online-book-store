from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile,Contact,JobListing,ApplyJob
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    birth_date= forms.DateField(widget=forms.DateInput(attrs={'type':'date','class':'forms-control'}))
    phone_number=forms.CharField(max_length=20)


    class Meta(UserCreationForm.Meta):
        model=User



class ContactForm(forms.ModelForm):
    
    class Meta:
        model= Contact
        fields=['first_name','last_name','Email','subject','message']
        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'Email':forms.EmailInput(attrs={'class':'form-control'}),
            'subject':forms.Textarea(attrs={'class':'form-control'}),
            'message':forms.Textarea(attrs={'class':'form-control'}),
    
        }
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['Email'].widget.attrs['placeholder'] = 'Enter a valid E-mail'

    


class JobListingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(JobListingForm, self).__init__(*args, **kwargs)
        self.fields['job_location'].widget.attrs['placeholder'] = 'USA,UK'
        self.fields['Salary'].widget.attrs['placeholder'] = '30K'
        self.fields['title'].widget.attrs['placeholder'] = 'Software Engineer, Web Designer'
        self.fields['application_deadline'].widget.attrs['placeholder'] = '2020-12-27'

    class Meta:
        model = JobListing
        
        exclude = ('user','image')
        labels = {
            "job_location": "Job Location",
            "published_on": "Publish Date"
        }
class JobApplyForm(forms.ModelForm):
    class Meta:
        model = ApplyJob
        fields = '__all__'
        labels = {
            "file": "CV (pdf format)",
            "name": "Full Name"

        }




