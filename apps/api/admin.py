from django.contrib import admin

from apps.api.models import User

# Register your models here.


@admin.register(User)
class UsersAdmin(admin.ModelAdmin):
    pass
