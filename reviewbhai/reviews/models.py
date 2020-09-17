from django.db import models
from django.urls import reverse
from django.utils.text import slugify


from accounts.models import models
from django.conf import settings
from django.utils import timezone


# Create your models here.
##model for tags
class Tag(models.Model):
    tag_name = models.CharField(max_length=50)
    date_added = models.DateTimeField(default=timezone.now)
    foods_or_travel = models.IntegerField()

    def __str__(self):
        return self.tag_name

## Model for food items
class Item(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    food_or_travel = models.CharField(max_length=20)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

##model for restaurent_or_place
class RestaurentOrPlace(models.Model):
    OPTIONS = (
        ('Restaurent', 'Restaurent'),
        ('Place','Place'),
    )
    name = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete = models.CASCADE)
    location = models.CharField(verbose_name= 'Location', null =True, max_length = 200)
    restaurent_place = models.CharField(max_length = 50, choices = OPTIONS)
    created_at = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.name.username



## Model for review
class Review(models.Model):
    review_title = models.CharField(verbose_name='Title', max_length=100)
    review_body = models.TextField()
    is_offer_or_planned = models.BooleanField(verbose_name='Offered or planned')
    is_recommended = models.BooleanField(verbose_name='Recommended')
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    time_posted = models.DateTimeField(default=timezone.now)
    post_or_discussion = models.CharField(max_length=20,null=None)
    food_or_travel = models.CharField(verbose_name='Foods or Travel',max_length=20)
    slug = models.SlugField(null=False,unique=True,max_length = 300)
    tags = models.ManyToManyField(Tag)
    items = models.ManyToManyField(Item)
    restaurentOrPlace = models.ForeignKey(RestaurentOrPlace, on_delete = models.CASCADE)

    def __str__(self):
        return self.review_title

    def get_absolute_url(self):
        return reverse('reviewdetails',kwargs={'slug': self.slug})

    def save(self,*args, **kwargs):
        author_id = str(self.author.id)
        time = str(self.time_posted)
        self.slug = slugify(time+'_'+self.review_title+author_id)
        return super().save(*args, **kwargs)

## model for stars
class Star(models.Model):
    post_id = models.ForeignKey(Review,related_name='post_review', on_delete = models.CASCADE )
    food = models.FloatField(verbose_name='Food',null=False)
    environment = models.FloatField(verbose_name='Food',null=False)
    service = models.FloatField(verbose_name='Food',null=False)
    cleanliness = models.FloatField(verbose_name='Food',null=False)


##models for reactions
class Reaction(models.Model):
    post_id = models.ForeignKey(Review, on_delete=models.CASCADE)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    is_liked = models.BooleanField(default=False)
    is_disliked = models.BooleanField(default=False)
    is_helpful = models.BooleanField(default=False)


def get_image_name(instance, imagename):
    title = instance.review.review_title
    slug = slugify(title)
    return "review_images/%s-%s" % (slug, imagename)

class Image(models.Model):
    review = models.ForeignKey(Review,default=None, on_delete = models.CASCADE)
    image = models.ImageField(upload_to=get_image_name,verbose_name='Image')




