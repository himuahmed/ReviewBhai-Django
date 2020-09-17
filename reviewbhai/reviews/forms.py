from django import forms
from .models import Review, Image, Star

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

## Stars Form

class StarsrForm(forms.ModelForm):
    food = forms.IntegerField(label='food')
    environment = forms.IntegerField(label='environment')
    service = forms.IntegerField(label='service')
    cleanliness = forms.IntegerField(label='cleanliness')

    class Meta:
        model = Star
        fields = ['food','environment','service','cleanliness']


class ReviewFullForm(ReviewForm):
    images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta(ReviewForm.Meta):
        fields = ReviewForm.Meta.fields + ['images',]


class UpdateReviewForm(ReviewForm):
    images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta(ReviewForm.Meta):
        fields = ReviewForm.Meta.fields + ['images',]
    def save(self, commit=True):
        review = self.instance
        if commit:
            review.save()

        return review

