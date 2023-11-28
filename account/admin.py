from django.contrib import admin
from .models import AccountAvatar, VerifiedUser, UserRating

class AdminView(admin.ModelAdmin):
    pass

class VerfiedAdminView(admin.ModelAdmin):
    list_display = ('username')

admin.site.register(VerifiedUser, AdminView)
admin.site.register(AccountAvatar, AdminView)
admin.site.register(UserRating, AdminView)