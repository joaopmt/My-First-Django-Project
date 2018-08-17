from django.db import models


# A classe aqui é como se fosse uma database table
class Product(models.Model):
    # define variáveis (table columns) e seus data types
    title = models.CharField(max_length=140)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    img = models.ImageField(upload_to='products/img')
    available = models.BooleanField(default=True)

    # Overrides the __str__() magic method
    def __str__(self):
        return self.title
