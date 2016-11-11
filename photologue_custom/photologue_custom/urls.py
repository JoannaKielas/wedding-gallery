from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls import *
from photologue.views import GalleryListView
from photologue.views import GalleryDetailView
from photologue.views import GalleryDateView
from photologue.views import PhotoListView
from photologue.views import PhotoDetailView
from photologue.views import PhotoDateView
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Examples:
    # url(r'^$', 'photologue_custom.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]

url(r'^photologue/', auth_views.login),