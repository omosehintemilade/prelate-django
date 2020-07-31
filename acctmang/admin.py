from django.contrib import admin
from django.contrib.auth.models import Group
from .models import User, Profile, UserEarnings, UserTransactionRecord


class UserModelAdmin(admin.ModelAdmin):
    list_display = ('email', 'account_number', 'date_joined', 'balance')
    search_fields = ["account_number"]


class UserEarningsModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'transaction_ref', 'datetime', 'amount_earned')
    search_fields = ["user__account_number"]
    autocomplete_fields = ["user"]


class UserTransactionRecordModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'transaction_type', 'amount', 'datetime')
    search_fields = ["user__account_number"]
    autocomplete_fields = ["user"]


admin.site.unregister(Group)
admin.site.register(User, UserModelAdmin)
admin.site.register(Profile)
admin.site.register(UserEarnings, UserEarningsModelAdmin)
admin.site.register(UserTransactionRecord, UserTransactionRecordModelAdmin)
