from django.contrib import admin

from .models import Products 

class PostAdmin(admin.ModelAdmin):
    list_display=('title','author','description','created_at','image')
    list_filter=('created_at',)
    search_fields=('title',)

admin.site.register(Products,PostAdmin)