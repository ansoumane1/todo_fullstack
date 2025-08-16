from django.db import models
import uuid

# Create your models here.

class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200, verbose_name="Titre")
    author = models.CharField(max_length=200, verbose_name="Auteur")
    isbn = models.CharField(max_length=17, blank=True, null=True, verbose_name="ISBN")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Prix", default=0.00)
    description = models.TextField(blank=True, verbose_name="Description")
    cover_image = models.URLField(blank=True, verbose_name="Image de couverture")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
