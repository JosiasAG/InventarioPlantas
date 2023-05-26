from django.forms import ModelForm
from . import models

class inventarioForms(ModelForm):
    class Meta:
        model = models.productsModel
        fields = ['product', 'description', 'category', 'initial_stock', 'price']
        verbose_name = 'ModelName'
        verbose_name_plural = 'ModelNames'
        


class incomingForm(ModelForm):
    class Meta:
        model = models.incomingProducts
        fields = ['bill', 'code', 'quantityIncoming','unit_price']
        verbose_name = 'ModelName'
        verbose_name_plural = 'ModelNames'
        

class outcomingForm(ModelForm):
    class Meta:
        model = models.outcomingProducts
        fields = ['bill', 'code', 'quantityOutcoming', 'unit_price']
        verbose_name = 'ModelName'
        verbose_name_plural = 'ModelNames'