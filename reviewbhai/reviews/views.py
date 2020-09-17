from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import  ListView, DetailView, UpdateView, DeleteView

from.models import Review, Image, Star
from .forms import ReviewForm, ImageForm, ReviewFullForm,UpdateReviewForm, StarsrForm
from django.forms import modelformset_factory
from django.http import HttpResponseRedirect

@login_required
def CreateReview(request):
    ImageFormSet = modelformset_factory(Image,form=ImageForm,extra=5)

    if request.method == 'POST':

        reviewForm = ReviewForm(request.POST)
        formset = ImageFormSet(request.POST,request.FILES,queryset=Image.objects.none())
        starsForm = StarsrForm(request.POST)


        if reviewForm.is_valid() and formset.is_valid() and starsForm.is_valid():
            review_form = reviewForm.save(commit=False)
            review_form.author = request.user
            review_form.post_or_discussion = 1
            review_form.food_or_travel = 'Foods'
            review_form.save()
            reviewForm.save_m2m()
            instance = review_form
            print(instance.id)
            star_form = starsForm.save(commit=False)
            star_form.post_id = instance
            star_form.save()

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
        starsForm = StarsrForm()
        formset = ImageFormSet(queryset=Image.objects.none())
    return render(request,'reviews/review_form.html',{'reviewForm':reviewForm,'formset':formset,'starsForm':starsForm})


# def UpdateReview(request,slug):
#     context = {}
#
#     user = request.user
#     if not user.is_authenticated:
#         return redirect("home")
#
#     review = get_object_or_404(Review,slug)
#     if request.POST:
#         form = UpdateReviewForm(request.POST or None, request.FILES or None)
#         if form.is_valid():
#             obj = form.save(commit=False)
#             obj.save()
#             context['success_message'] = "Review Updated"
#             review = obj
#
#     form = UpdateReviewForm







class ShowReviews(ListView):
    # model = Review
    template_name = 'reviews/home.html'
    context_object_name = 'reviews'
    ordering = ['-time_posted']
    queryset = Review.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ShowReviews,self).get_context_data(**kwargs)
        context['stars'] = Star.objects.all()
        return context

# class ShowStars(ListView):
#     model = Star
#     template_name = 'reviews/home.html'
#     context_object_name = 'stars'

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


