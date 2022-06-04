from django.db import models
from apps.account.models import CustomUser
from apps.product.models import Product


class Review(models.Model):
    author = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE, related_name='reviews')
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)
    
    def __str__(self):
        return f'{self.author.email}{self.text}'