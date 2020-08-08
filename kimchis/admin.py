from django.contrib import admin
from .models import Kimchi, MainIngredient, Tag

# Register your models here.
admin.site.register(Kimchi)
admin.site.register(MainIngredient)
admin.site.register(Tag)


