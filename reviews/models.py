from django.db import models
from kimchis.models import Kimchi


# Create your models here.
class Review(models.Model):
    title = models.CharField(blank=False, max_length=255)
    product_name = models.ForeignKey(Kimchi, on_delete=models.CASCADE)
    content = models.TextField(blank=False)
    published = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title




