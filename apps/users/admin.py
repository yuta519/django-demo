from django.contrib import admin

from apps.users.models import User

# Register your models here.

# admin.site.register(User)


@admin.register(User)
class UsersAdmin(admin.ModelAdmin):
    pass
