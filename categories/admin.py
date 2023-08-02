from django.contrib import admin
from .models import Category, Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'available', 'category')
    list_filter = ('category', 'available')
    search_fields = ('name', 'description')
    list_per_page = 20

    def description(self, obj):
        return obj.description

    def available(self, obj):
        return obj.available

    description.short_description = 'Description'
    available.short_description = 'Available'

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)

admin.site.site_header = 'OmAutoandTyres Admin'
admin.site.site_title = 'OmAutoandTyres Admin'
admin.site.index_title = 'Welcome to OmAutoandTyres Admin'
