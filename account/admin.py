from django.contrib import admin
# from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

from account.models import AccountUser, Profile

# Register your models here.
class UserCustomAdmin(UserAdmin):
    # de them truong image luc create user        
        fieldsets = (
        (
        (None, {'fields': ('username', 'password')}), 
        ('Personal info', {'fields': ('first_name', 'last_name', 'email',)}),
        )
        )

        # fieldsets = ()
        list_display = ('username','email', 'is_staff', 'is_active')
        list_filter = ('email', 'is_staff', 'is_active',)

admin.site.register(Profile)

admin.site.register(AccountUser, UserCustomAdmin)

