from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from datetime import date
from kimchis.models import Kimchi


# Create your models here.
class Review(models.Model):
    title = models.CharField(blank=False, max_length=255)
    product_name = models.ForeignKey(Kimchi, on_delete=models.CASCADE)
    content = models.TextField(blank=False)
    published = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    last_updated = models.DateField(blank=True, default=date.today)
    cover = CloudinaryField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.last_updated = date.today()
        super().save(*args, **kwargs)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(blank=False)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[0:50]
