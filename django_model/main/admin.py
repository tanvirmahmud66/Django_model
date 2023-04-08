from django.contrib import admin
from .models import Profile, PostDB
# Register your models here.


class ProfileView(admin.ModelAdmin):
    list_display = ('id', 'user', 'userId', 'bio', 'gender', 'profession',
                    'workplace', 'relationStatus')


class PostView(admin.ModelAdmin):
    list_display = ('profile', 'body', 'created', 'updated')


admin.site.register(Profile, ProfileView)
admin.site.register(PostDB, PostView)
