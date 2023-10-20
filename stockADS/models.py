from django.db import models

class Categorias(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    
    class Meta:
        verbose_name = 'Categories'
        verbose_name_plural = 'Categories'   

class Products(models.Model):

    # itens = [
    #     ('1', 'P'),
    #     ('2', 'M'),
    #     ('3', 'G'),
    #     ('4', 'GG'),
    # ]


    name = models.CharField(max_length=255)
    caregory = models.ForeignKey(Categorias, on_delete=models.CASCADE, blank=True)
    picture = models.ImageField(blank=False)
    cod = models.IntegerField(unique=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField()
    qtd = models.IntegerField()
    # size = models.CharField(choices=itens, max_length=255)
    discount = models.IntegerField()
    created_at = models.DateField()
    in_stock = models.BooleanField(default=False)

    def _str_(self):
        return self.nome 
    
    class Meta:
            verbose_name = 'Products'
            verbose_name_plural = 'Products'    
    


    

