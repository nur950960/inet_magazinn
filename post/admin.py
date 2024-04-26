from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display=('title','author','description','created_at','image')
    list_filter=('created_at',)
    search_fields=('title','author',)
admin.site.register(Post,PostAdmin)
