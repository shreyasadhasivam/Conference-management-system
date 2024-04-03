from django.contrib import admin
from .models import Paper
from conference_management.models import UserProfile

admin.site.register(Paper)
admin.site.register(UserProfile)
