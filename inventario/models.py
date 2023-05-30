from django.db import models
from django.db.models import Sum

class productsModel(models.Model):
    
    category_plants = (
        ('0', 'Árboles y arbustos'),
        ('1', 'Césped y tapizantes'),
        ('2', 'Anuales'),
        ('3', 'Florales'),
        ('4', 'Palmeras'),
        ('5', 'Helechos'),
        ('6', 'Trepadoras'),
        ('7', 'Acuáticas'),
    )
    
    
    product = models.CharField('Producto' ,max_length=100)
    description = models.TextField('Descripción', max_length=400)
    category = models.CharField('Categoría', max_length=1, choices=category_plants)
    price = models.IntegerField('Precio público', default=0)
    initial_stock = models.IntegerField('Stock inicial')
    incomings = models.IntegerField('Entradas') 
    outcomings = models.IntegerField('Salidas')
    summatory = models.IntegerField('Existencias')
    
    def __str__(self):
        return str(self.pk) + ' - ' + self.product
    
    def save(self, *args, **kwargs):
        incoming_products = incomingProducts.objects.filter(code=self)
        outcoming_products = outcomingProducts.objects.filter(code=self)
        self.incomings = incoming_products.aggregate(Sum('quantityIncoming')).get('quantityIncoming__sum') or 0
        self.outcomings = outcoming_products.aggregate(Sum('quantityOutcoming')).get('quantityOutcoming__sum') or 0
        self.summatory = (self.incomings + self.initial_stock) - self.outcomings
        super(productsModel, self).save(*args, **kwargs)

    


class incomingProducts(models.Model):
    supplier = models.CharField(("Proveedor"), max_length=100, default='')
    name = models.CharField(("Nombre o razón social"), max_length=100, default='')
    address = models.CharField(("Dirección"), max_length=100, default='')
    telephone = models.CharField(("Teléfono"), max_length=15, default='')
    email = models.EmailField(("Correo electrónico"), max_length=100, default='')
    bill = models.CharField('No. factura compra' ,max_length=10, default='')
    dateIncoming = models.DateTimeField('Fecha ingreso' ,auto_now=False, auto_now_add=True)
    code = models.ForeignKey(productsModel, verbose_name=("Producto"), on_delete=models.CASCADE)
    quantityIncoming = models.IntegerField('Cantidad ingresada')
    unit_price = models.DecimalField('Precio', max_digits=10, decimal_places=2)
    
    
    def __str__(self):
        return 'No. Factura: ' + self.bill + ' - ' + str(self.dateIncoming)
    
    

class outcomingProducts(models.Model):
    bill = models.CharField('No. factura venta',max_length=10)
    dateOutcoming = models.DateTimeField('Fecha salida',auto_now=False, auto_now_add=True)
    code = models.ForeignKey(productsModel, verbose_name=("Producto"), on_delete=models.CASCADE)
    quantityOutcoming = models.IntegerField('Cantidad salida')
    unit_price = models.IntegerField('Precio', default = 0)
        
    
    def __str__(self):
        return 'No. Factura: SDLP' + self.bill + ' - ' + str(self.dateOutcoming)