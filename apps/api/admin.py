from django.contrib import admin

from apps.api.models.user_models import User


@admin.register(User)
class UsersAdmin(admin.ModelAdmin):
    pass
