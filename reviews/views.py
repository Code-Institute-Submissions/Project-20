from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from .models import Review
from .forms import ReviewForm


def all_reviews(request):
    reviews = Review.objects.all()
    return render(request, 'reviews/all_reviews.template.html', {
        'reviews': reviews
    })


def create_review(request):
    if request.method == 'POST':
        print(request.POST)

        create_form = ReviewForm(request.POST)

        if create_form.is_valid():
            create_form.save()
            return redirect(reverse(all_reviews))
        else:
            return render(request, 'reviews/create_review.template.html', {
                'form': create_form
            })
    else:
        create_form = ReviewForm()
        return render(request, 'reviews/create_review.template.html', {
            'form': create_form
        })


def review_details(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    return render(request, 'reviews/review_details.template.html', {
        'review': review
    })


def update_review(request, review_id):
    review_being_updated = get_object_or_404(Review, pk=review_id)

    if request.method == 'POST':
        review_form = ReviewForm(request.POST, instance=review_being_updated)
        if review_form.is_valid():
            review_form.save()
            return redirect(reverse(all_reviews))
        else:
            return render(request, 'reviews/update_review.template.html', {
                'form': review_form
            })
    else:
        review_form = ReviewForm(instance=review_being_updated)
        return render(request, 'reviews/update_review.template.html', {
            'form': review_form,
            'review': review_being_updated
    })




