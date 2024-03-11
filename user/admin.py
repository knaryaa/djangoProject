from django.contrib import admin
from user.models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'address', 'phone_number', 'city', 'country', 'image_tag']


admin.site.register(UserProfile, UserProfileAdmin)