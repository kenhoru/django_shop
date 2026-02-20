from django.db import models


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="цена")
    image = models.ImageField(upload_to="products/", verbose_name="Изображение")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
