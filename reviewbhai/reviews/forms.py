from django import forms
from .models import Review, Image

class ReviewForm(forms.ModelForm):
    review_title = forms.CharField(max_length=100)

    class Meta:
        model = Review
        fields = ['restaurentOrPlace','review_title','review_body','tags','items','is_offer_or_planned','is_recommended']

class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')

    class Meta:
        model = Image
        fields = ('image', )


class ReviewFullForm(ReviewForm):
    images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta(ReviewForm.Meta):
        fields = ReviewForm.Meta.fields + ['images',]


class UpdateReviewForm(ReviewFullForm):
    images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta(ReviewForm.Meta):
        fields = ReviewForm.Meta.fields + ['images',]
    def save(self, commit=True):
        review = self.instance
        if commit:
            review.save()
        return review

