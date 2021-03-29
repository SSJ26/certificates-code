from django.contrib import admin

# Register your models here.
from .models import *

class Person_list(admin.ModelAdmin):
    list_display=['firstName','secondName','course','courseDetails','companyLink','date','companyName','ceoName']
admin.site.register(Person,Person_list)