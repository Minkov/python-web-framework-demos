from django.contrib import admin

from common_tools.web.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


# admin.site.register(Profile, ProfileAdmin)
