from django.contrib import admin

# Register your models here.
from .models import Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields = ('name', 'description')

admin.site.register(Category, CategoryAdmin)