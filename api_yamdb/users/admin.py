from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    """Админка пользователей."""

    list_display = (
        "username",
        "id",
        "email",
        "first_name",
        "last_name",
        "bio",
        "role",
    )
    search_fields = (
        "username",
        "role",
    )


admin.site.register(User, UserAdmin)
