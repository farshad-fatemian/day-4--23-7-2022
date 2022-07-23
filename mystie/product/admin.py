from django.contrib import admin

from .models import Product , comments

# Register your models here.

class commentinline(admin.StackedInline):
    model = comments
    
    
class ProductAdmin(admin.ModelAdmin):
    inlines = [commentinline]


admin.site.register(Product,ProductAdmin)
admin.site.register(comments)
