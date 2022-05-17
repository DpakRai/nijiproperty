from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import NijiUserCreationForm, NijiUserChangeForm

User = get_user_model()

class NijiUserAdmin(UserAdmin):
    add_form = NijiUserCreationForm
    form = NijiUserChangeForm
    model = User
    list_display = ['username', 'email']
    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('profile_picture', 'is_buyer')}),
    ) #this will allow to change these fields in admin module


admin.site.register(User, NijiUserAdmin)
