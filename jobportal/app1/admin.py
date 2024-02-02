
from django.contrib import admin
from.models import JobListing
from.models import UserProfile
from.models import Contact
from.models import ApplyJob
from django.utils.html import format_html



admin.site.register(UserProfile)
admin.site.register(Contact)
admin.site.register(ApplyJob)
# admin.site.register(JobListing)


class JobListingAdmin(admin.ModelAdmin):
    list_display=['title','company_name']
    ordering=['title']



admin.site.register(JobListing,JobListingAdmin)



