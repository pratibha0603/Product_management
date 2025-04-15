from django.contrib import admin
from .models import Release, Patch, Product, Image



@admin.register(Release)
class ReleaseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(Patch)
class PatchAdmin(admin.ModelAdmin):
    list_display = ('name', 'release', 'description')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'patch', 'status')

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('image_url', 'product')
