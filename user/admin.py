from django.contrib import admin

from .models import User

class AdminView(admin.ModelAdmin):
    pass

admin.site.register(User, AdminView)