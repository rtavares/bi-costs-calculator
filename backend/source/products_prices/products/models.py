from django.contrib.auth.models import User
from django.db import models


class Common(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, related_name="author", on_delete=models.CASCADE, null=True, blank=True
    )
    last_modified_by = models.ForeignKey(
        User, related_name="editor", on_delete=models.CASCADE, null=True, blank=True
    )


class Product(Common):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
