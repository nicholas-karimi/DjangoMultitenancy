from django.contrib import admin

from .models import Item, SiteSettings


admin.site.register(Item)
admin.site.register(SiteSettings)

