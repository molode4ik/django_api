from django.contrib import admin
from .models import Teaser


class TeaserAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'category', 'author', 'status')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title', 'category')


admin.site.register(Teaser, TeaserAdmin)
