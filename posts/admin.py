from django.contrib import admin

from .models import Post, Site, Item, Image

admin.site.register([ Post, Site, Item, Image])