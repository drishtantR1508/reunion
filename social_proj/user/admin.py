from django.contrib import admin
from django.contrib.auth.models import User,Group
from .models import UserProfileInfo

# Register your models here.
admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(User)
admin.site.register(UserProfileInfo)
