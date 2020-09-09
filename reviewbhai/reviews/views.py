from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import  ListView, DetailView, UpdateView, DeleteView

from.models import Review, Image
from .forms import ReviewForm, ImageForm
from django.forms import modelformset_factory
from django.http import HttpResponseRedirect

@login_required
def CreateReview(request):
    ImageFormSet = modelformset_factory(Image,form=ImageForm,extra=5)

    if request.method == 'POST':
        reviewForm = ReviewForm(request.POST)
        formset = ImageFormSet(request.POST,request.FILES,queryset=Image.objects.none())

        if reviewForm.is_valid() and formset.is_valid():
            review_form = reviewForm.save(commit=False)
            review_form.author = request.user
            review_form.save()

            for form in formset.cleaned_data:
                if form:
                    image = form['image']
                    photo = Image(review=review_form,image=image)
                    photo.save()
            messages.success(request,'Image Uploaded Successfully')
            return HttpResponseRedirect("/")
        else:
            print(reviewForm.errors, formset.errors)
    else:
        reviewForm = ReviewForm()
        formset = ImageFormSet(queryset=Image.objects.none())
    return render(request,'reviews/review_form.html',{'reviewForm':reviewForm,'formset':formset})





class ShowReviews(ListView):
    model = Review
    template_name = 'reviews/home.html'
    context_object_name = 'reviews'
    ordering = ['-time_posted']

class ReviewDetails(DetailView):
    model = Review
    slug_field = 'slug'
    time = str(Review.time_posted)
    prepopulated_fields = {'slug':('time+title+"Review.author.id"',)}
    #self.slug = slugify(time + '_' + self.review_title + author_id)

class UpdateReview(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Review
    fields = ['review_title','review_body','is_offer_or_planned','is_recommended','tags','items']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post_or_discussion = 'review'
        form.instance.food_or_travel = 'food'
        return super().form_valid(form)

    def test_func(self):
        review = self.get_object()
        if self.request.user == review.author:
            return True
        else:
            return False

class DeleteReview(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Review
    success_url = '/'

    def test_func(self):
        review = self.get_object()
        if self.request.user == review.author:
            return True
        else:
            return False


