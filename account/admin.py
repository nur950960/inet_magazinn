from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import User
# User=get_user_model()

# admin.site.register(User)

# User=get_user_model=()
class UserAdmin(admin.ModelAdmin):
    list_display=('email','last_name','first_name')
    list_filter=('is_active',)
    search_fields=('email',)


admin.site.register(User,UserAdmin)
