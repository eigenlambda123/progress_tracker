from django.contrib import admin
from .models import CustomUser, Profile

admin.site.register(CustomUser)
admin.site.register(Profile)

# Mix profile with user
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'