from django.contrib import admin

# Register your models here.
from . models import book
from django.utils.html import format_html
class bookadmin(admin.ModelAdmin):
    list_display=['title','price','display_image']
    ordering=['price']



    def display_image(self,obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />',obj.image.url)
        return None
    
    display_image.short_description='image'
#     ordering=['price']
#     site_header='Your Project Name Admin'
#     site_title='Your Project Name Admin'
#     def image(self,obj):
#         if obj.image:
#             return format_html('<img src="{}" width)
#         return None
#     image
        
admin.site.register(book,bookadmin)






