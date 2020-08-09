from django.db import models
from django.contrib.auth.models import User
from kimchis.models import Kimchi


# Create your models here.
class Review(models.Model):
    title = models.CharField(blank=False, max_length=255)
    product_name = models.ForeignKey(Kimchi, on_delete=models.CASCADE)
    content = models.TextField(blank=False)
    published = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title




