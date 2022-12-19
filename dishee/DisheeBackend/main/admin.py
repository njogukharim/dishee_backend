from django.contrib import admin
from .models import User, Comment, Order, Recipe
from django.contrib.auth.admin import UserAdmin as BaseAdmin
from django.contrib.auth import get_user_model
# Register your models here.

class UserAdmin(BaseAdmin):
    add_fieldsets = (
        (None,{
            'classes' : ('wide',),
            'fields' : ('username', 'email','phone_no','password1','password2')
        }),
    )

admin.site.register(get_user_model(), UserAdmin)
admin.site.register(Order)
admin.site.register(Comment)
admin.site.register(Recipe)