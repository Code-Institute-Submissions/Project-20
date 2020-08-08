from django.shortcuts import render, HttpResponse
from .models import Review


# Create your views here.
def all_reviews(request):
    reviews = Review.objects.all()
    return render(request, 'reviews/all_reviews.template.html', {
        'reviews': reviews
    })

