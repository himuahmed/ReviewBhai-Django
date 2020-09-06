# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.views.generic import CreateView, ListView, DetailView
#
# from.models import Review
#
#
#
# class CreateReview(LoginRequiredMixin,CreateView):
#     model = Review
#     fields = ['review_title','review_body','is_offer_or_planned','is_recommended','tags','items']
#
#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         form.instance.post_or_discussion = 'review'
#         form.instance.food_or_travel = 'food'
#         return super().form_valid(form)
#
# class ShowReviews(ListView):
#     model = Review
#     template_name = 'reviews/home.html'
#     context_object_name = 'reviews'
#     ordering = ['-time_posted']
#
# class ReviewDetails(DetailView):
#     model = Review
#     slug_field = 'slug'
#     time = str(Review.time_posted)
#     prepopulated_fields = {'slug':('time+title+"Review.author.id"',)}
#     #self.slug = slugify(time + '_' + self.review_title + author_id)