from django.contrib import admin
from .models import User
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')
    list_filter = ('username',)
    #prepopulated_fields = {'slug': ('title',)}

admin.site.register(User, UserAdmin)