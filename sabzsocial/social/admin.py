from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin


# Register your models here.

@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ['username','phone','first_name','last_name']
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Information',{'fields':('date_of_birth','bio','photo','job','phone')}),
    )
@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ['name','subject','phone']