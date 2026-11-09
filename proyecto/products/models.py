from django.db import models

class Product(models.Model):
    name = models.CharField(
        null=False, blank=False, unique=True
    )
    description = models.TextField()
    price = models.IntegerField(
        null=True,
        blank=True,
        default=0
    )
    stock = models.IntegerField(
        null=True,
        blank=True,
        default=0
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )
    def __str__(self):
        return self.name