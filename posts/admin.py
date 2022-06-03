from django.contrib import admin

from .models import Site, Post, Item

admin.site.register([ Site, Post, Item])