from django.contrib import admin

from retailing.models import Dealer, Product


@admin.register(Dealer)
class DealerAdmin(admin.ModelAdmin):
    readonly_fields = ('level',)
    list_display = ('title', 'supplier', 'debt', 'date_created')
    list_filter = ('city',)
    actions = ['clean_debt']

    def clean_debt(self, request, queryset):
        queryset.update(debt=0)

    clean_debt.short_description = 'Погасить задолженность'

admin.site.register(Product)
