from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Review, Comment
from .forms import ReviewForm, CommentForm


def all_reviews(request):
    reviews = Review.objects.all()
    return render(request, 'reviews/all_reviews.template.html', {
        'reviews': reviews
    })


@login_required
def create_review(request):
    if request.method == 'POST':
        print(request.POST)

        create_form = ReviewForm(request.POST)

        if create_form.is_valid():
            review = create_form.save(commit=False)
            review.user = request.user
            review.save()
            messages.success(
                request, "New review posted successfully!")
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
    comments = Comment.objects.all().filter(review=review)
    return render(request, 'reviews/review_details.template.html', {
        'review': review,
        'comments': comments
    })


@login_required
def update_review(request, review_id):
    review_being_updated = get_object_or_404(Review, pk=review_id)

    if review_being_updated.user == request.user:
        review_being_updated = get_object_or_404(Review, pk=review_id)

        if request.method == 'POST':
            review_form = ReviewForm(
                request.POST, instance=review_being_updated)
            if review_form.is_valid():
                review_form.save()
                messages.success(
                    request, "Review updated successfully!")
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
    else:
        return HttpResponse("You are not allowed. This reveiw is not yours.")


@login_required
def delete_review(request, review_id):
    review_to_delete = get_object_or_404(Review, pk=review_id)

    if review_to_delete.user == request.user:
        review_to_delete = get_object_or_404(Review, pk=review_id)

        if request.method == "POST":
            review_to_delete.delete()
            messages.success(
                request, "Review deleted successfully!")
            return redirect(reverse(all_reviews))
        else:
            return render(request, 'reviews/delete_review.template.html', {
                'review': review_to_delete
            })
    else:
        return HttpResponse("You are not allowed. This review is not yours.")


@login_required
def create_comment(request, review_id):
    review = get_object_or_404(Review, pk=review_id)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.review = review
            comment.user = request.user
            comment.save()
            messages.success(
                request, "New comment registered successfully!")
            return redirect(reverse(review_details, args=(review_id, )))
        else:
            return HttpResponse("Error with forms")
    else:
        form = CommentForm()
        return render(request, 'reviews/create_comment.template.html', {
            'form': form,
            'review': review
        })
