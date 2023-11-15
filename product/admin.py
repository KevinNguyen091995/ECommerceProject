from django.contrib import admin
from .models import Product

class AdminView(admin.ModelAdmin):
    pass

admin.site.register(Product, AdminView)