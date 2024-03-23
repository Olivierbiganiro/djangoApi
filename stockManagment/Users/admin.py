from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    model = User
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('name',)}),
    )  # Add 'name' to the user edit form in admin

admin.site.register(User, CustomUserAdmin)
