from django.contrib import admin

from retailing.models import Dealer, Product


@admin.register(Dealer)
class DealerAdmin(admin.ModelAdmin):
    readonly_fields = ('level',)
    list_display = ('title', 'supplier', 'debt', 'date_created')
    list_filter = ('city',)


admin.site.register(Product)
