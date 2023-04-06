from django.contrib import admin
from .models import Profile
# Register your models here.


class ProfileView(admin.ModelAdmin):
    list_display = ('id', 'user', 'userId', 'bio', 'gender', 'profession',
                    'workplace', 'relationStatus')


admin.site.register(Profile, ProfileView)
