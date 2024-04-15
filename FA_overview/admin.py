from django.contrib import admin
from .models import Profile, Beep

from .models import Profile, Client, Transaction, Beep


# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'Bio', 'Industry', 'investment_preference', "profile_type"]
    search_fields = ['user__username']


# Register Beeps
admin.site.register(Beep)
