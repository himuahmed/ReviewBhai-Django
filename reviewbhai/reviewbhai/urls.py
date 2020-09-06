"""reviewbhai URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from accounts.views import login_view,register_view, logout_view, profile_view, updateprofile_view
from reviews.views import CreateReview, ReviewDetails, ShowReviews, UpdateReview, DeleteReview

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',include('reviews.urls')),
    path('login/',login_view,name='login'),
    path('logout/',logout_view,name='logout'),
    path('register/',register_view,name='registration'),
    path('profile/<username>',profile_view,name='profile'),
    path('editprofile/',updateprofile_view,name='editprofile'),

    #password related urls
    path('changepassword/', auth_views.PasswordChangeView.as_view(template_name='accounts/password_change.html'), name='password_change'),
    path('password-updated/', auth_views.PasswordChangeDoneView.as_view(template_name='accounts/password_updated.html'), name='password_change_done'),

    path('resetpass/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'),name='resetpassword'),
    path('resetpass/done', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),name='password_reset_done'),
    path('resetpassconfirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),name='password_reset_confirm'),
    path('resetpasscomplete/',auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),name='password_reset_complete'),

    ##Review Related urls
    path('',ShowReviews.as_view(),name='home'),
    path('postreview/',CreateReview.as_view(),name='createreview'),
    path('reviewdetails/<slug:slug>/',ReviewDetails.as_view(),name='reviewdetails'),
    path('updatereview/<slug:slug>/',UpdateReview.as_view(),name='reviewupdate'),
    path('deletereview/<slug:slug>/',DeleteReview.as_view(),name='reviewdelete'),



    #path('user/',include('accounts.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)