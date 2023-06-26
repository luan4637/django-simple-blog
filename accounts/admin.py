import imp
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import AccountChangeForm, AccountCreationForm
from .models import Account

class AccountAdmin(UserAdmin):
    model = Account
    search_fields = ('email', 'first_name', 'last_name',)
    ordering = ('-date_joined',)
    list_display = ('email', 'first_name', 'last_name', 'date_joined', 'is_active',)
    list_filter = ()
    fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name', 'email', 'groups', 'password', 'is_active')
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'email', 'groups', 'password1', 'password2', 'is_active')}
        ),
    )
    add_form = AccountCreationForm
    form = AccountChangeForm

# Register your models here.
admin.site.register(Account, AccountAdmin)