from django.contrib import admin

from my_music_app2.users.models import Profile


# Register your models here.

@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    pass
