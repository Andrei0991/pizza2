from django.db import models


# Create your models here.

class Product(models.Model):
        CATEGORY = (
                        ('Neapolitan Pizza', 'Neapolitan Pizza'),
                        ('Chicago Pizza', 'Chicago Pizza'),
                        ('New York-Style Pizza', 'New York-Style Pizza'),
                        ('Greek Pizza', 'Greek Pizza'),
                        ('California Pizza', 'California Pizza'),
                        ('Capricciosa Pizza', 'Capricciosa Pizza'),
                        ('Mexican Pizza', 'Mexican Pizza'),
                        ('Quattro Stagioni Pizza', 'Quattro Stagioni Pizza'),
                        ('Quattro Formaggi Pizza', 'Quattro Formaggi Pizza'),
                )
                
        
        name = models.CharField(max_length=255, null=True, choices=CATEGORY)
        fields = models.ImageField(upload_to ='', null=True)
        description = models.CharField(max_length=250, null=True, blank=True)
        
        
        

        def __str__(self):
                return self.name
    


class Order(models.Model):
        STATUS = (
                ('ACTIVA', 'ACTIVA'),
                ('FINALIZATA', 'FINALIZATA'),
        )
        
        

        name = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
        date_created = models.DateField(auto_now_add=True, null=True)
        status = models.CharField(max_length=250, null=True, choices=STATUS, default='ACTIVA')
        
        
        


        def __str__(self):
            return str(self.id)
        
        
        


class Order_product(models.Model):
        SIZES = (
            ('Small', 'Small'),
            ('Medium', 'Medium'),
            ('Large', 'Large'),
            ('Extra Large', 'Extra Large')
            )
        product  = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
        orders   = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
        quantity = models.IntegerField(default = 1)
        size     = models.CharField(max_length=255, null=True, choices=SIZES)
       

class Price(models.Model):
        size     = models.CharField(max_length=255, null=True)
        price = models.DecimalField(default=1, decimal_places=2, max_digits=5)       
        

