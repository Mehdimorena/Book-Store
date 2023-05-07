from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    # che jozeeyati az karbar ha ro neshun bede tuye panel modiriyate userha
    list_display = ['username', 'email', 'age', 'is_staff']

    # age ro be field haye panel khode user ezafe mikone
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('age',)}),
    )

    # age ro be panel add new user ezafe mikone
    add_fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('age',)}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
