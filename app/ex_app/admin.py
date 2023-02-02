from django.contrib import admin
from .models import Teaser, Author


class TeaserAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'category', 'status')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title', 'category')


class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'money')
    list_display_links = ('id', 'money')
    search_fields = ('id', 'money')


admin.site.register(Teaser, TeaserAdmin)
admin.site.register(Author, UsersAdmin)
