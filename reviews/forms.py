from django import forms
from .models import Review, Comment
from cloudinary.forms import CloudinaryJsFileField


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('title', 'product_name', 'content', 'cover')
    cover = CloudinaryJsFileField()


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
