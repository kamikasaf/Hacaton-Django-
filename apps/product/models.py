from django.db import models
from django.contrib.auth import get_user_model


from apps.category.models import Category

User = get_user_model()


class Product(models.Model):

    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='products')
    title = models.CharField(max_length=100)
    desc = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, related_name='products')
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
            verbose_name='Продукт'
            verbose_name_plural="Продукты"