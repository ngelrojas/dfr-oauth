from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

from .models.user import User


class UserAdmin(BaseUserAdmin):
    """panel admin"""

    ordering = ["id"]
    list_display = ["email", "first_name", "last_name"]
    list_filter = []
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal Info"), {"fields": ("first_name", "last_name",)}),
        (_("Permissions"), {"fields": ("is_activate", "is_staff", "is_superuser")}),
        (_("Important dates"), {"fields": ("last_login",)}),
    )

    add_fieldsets = (
        (None, {"classes": ("wide",), "fields": ("email", "password1", "password2")}),
    )


admin.site.register(User, UserAdmin)
