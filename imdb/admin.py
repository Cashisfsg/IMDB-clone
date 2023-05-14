from django.contrib import admin

from .models import *


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ['last', 'first']


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'year', 'rating', 'director']
    list_filter = ['director']
    prepopulated_fields = {'slug': ('title', 'year')}


@admin.register(UserAddon)
class UserAddonAdmin(admin.ModelAdmin):
    list_display = ['user']


@admin.register(MovieComment)
class MovieCommentAdmin(admin.ModelAdmin):
    list_display = ['text', 'movie', 'published', 'author']