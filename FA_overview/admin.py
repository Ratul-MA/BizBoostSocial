from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile, Beep

# Unregister Groups
admin.site.unregister(Group)


# Mix Profile info into User info
class ProfileInline(admin.StackedInline):
    model = Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'Bio', 'Industry', 'investment_preference', "profile_type"]
    search_fields = ['user__username']


# Register Beeps
admin.site.register(Beep)
