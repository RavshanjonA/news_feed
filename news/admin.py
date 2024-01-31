from django.contrib import admin

from news.models import New


@admin.register(New)
class NewsAdmin(admin.ModelAdmin):
    pass
