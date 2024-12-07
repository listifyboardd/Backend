from django.contrib import admin

from src.apps.users.models import CustomUser

admin.site.register(CustomUser)

