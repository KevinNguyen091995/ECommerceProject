from django.contrib import admin
from .models import AccountAvatar

class AdminView(admin.ModelAdmin):
    pass

admin.site.register(AccountAvatar, AdminView)