from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("name", "email", "phone", "is_staff", "is_active",)
    list_filter = ("name", "email", "phone", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("name", "email",  "phone", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_superuser", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "name", "email", "phone", "password1", "password2", "is_staff", "is_superuser",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(CustomUser, CustomUserAdmin)