from django.contrib import admin
from .models import category
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_field = {'slug': ('category_name',)}
    list_display = ('category_name', 'slug')
admin.site.register(category, CategoryAdmin)
