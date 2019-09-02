from django.contrib import admin
from paper_admin.admin.sortable import SortableAdminMixin
from .models import Page


@admin.register(Page)
class PageAdmin(SortableAdminMixin, admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': (
                'header',
            ),
        }),
    )
    sortable = 'order'
    search_fields = ['header']
