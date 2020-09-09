from django import forms
from .models import Review, Image

class ReviewForm(forms.ModelForm):
    review_title = forms.CharField(max_length=100)

    class Meta:
        model = Review
        fields = ('review_title','review_body','tags','items','is_offer_or_planned','is_recommended')

class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')

    class Meta:
        model = Image
        fields = ('image', )