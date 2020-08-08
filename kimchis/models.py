from django.db import models


# Create your models here.
class Kimchi(models.Model):
    title = models.CharField(blank=False, max_length=255)
    desc = models.TextField(blank=False)
    price = models.FloatField(blank=False)
    manufactured_date = models.DateField(blank=False)
    expiry_date = models.DateField(blank=False)

    def __str__(self):
        return self.title + " " + self.desc

