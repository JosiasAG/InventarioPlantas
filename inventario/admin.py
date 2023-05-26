from django.contrib import admin
from . import models

class productsModelAdmin(admin.ModelAdmin):
    readonly_fields = ('summatory', 'incomings', 'outcomings',)


admin.site.register(models.productsModel, productsModelAdmin)
admin.site.register(models.incomingProducts)
admin.site.register(models.outcomingProducts)


