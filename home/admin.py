from django.contrib import admin
from .models import contact 
# Register your models here.
admin.site.register(contact)

# class contactAdmin(admin.ModelAdmin):
#     list_display = ['sno','name','email']