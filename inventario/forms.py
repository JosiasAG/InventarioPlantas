from django.forms import ModelForm
from . import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class userForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
    



class inventarioForms(ModelForm):
    class Meta:
        model = models.productsModel
        fields = ['product', 'description', 'category', 'initial_stock', 'price']
        verbose_name = 'ModelName'
        verbose_name_plural = 'ModelNames'
        


class incomingForm(ModelForm):
    class Meta:
        model = models.incomingProducts
        fields = ['supplier', 'name', 'address', 'telephone', 'email', 'bill', 'code', 'quantityIncoming','unit_price']
        verbose_name = 'ModelName'
        verbose_name_plural = 'ModelNames'      

class outcomingForm(ModelForm):
    class Meta:
        model = models.outcomingProducts
        fields = ['code', 'quantityOutcoming', 'unit_price']
        verbose_name = 'ModelName'
        verbose_name_plural = 'ModelNames'