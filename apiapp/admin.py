from django.contrib import admin
from .models import AccountHistory
# Register your models here.

class AccountHistoryAdmin(admin.ModelAdmin):
    list_display = ('amount', 'date', 'category', 'type', 'description',)
    #list_filter = ('username',)
    #prepopulated_fields = {'slug': ('title',)}

admin.site.register(AccountHistory, AccountHistoryAdmin)