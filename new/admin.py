from django.contrib import admin
from .models import *



# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display=("last_name","name",)
admin.site.register(Author,AuthorAdmin)
class BookAdmin(admin.ModelAdmin):
    list_display=('title','status',)
admin.site.register(Book,BookAdmin)
class GenreAdmin(admin.ModelAdmin):
    list_display=('name','slug')
admin.site.register(Genre,GenreAdmin)




