from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from.models import Account,Profile

class CustomUserAdmin(UserAdmin):
    list_display = ('username','fullname','gender','email','contact','location','date_joined','last_login','is_admin','is_staff',)
    search_fields = ('username','fullname','email')
    read_only = ('date_joined','last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account,CustomUserAdmin)
admin.site.register(Profile)


# Register your models here.
