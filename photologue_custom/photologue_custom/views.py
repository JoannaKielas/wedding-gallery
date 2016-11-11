from photologue.views import GalleryListView
from photologue.views import GalleryDetailView
from photologue.views import GalleryDateView
from photologue.views import PhotoListView
from photologue.views import PhotoDetailView
from photologue.views import PhotoDateView
from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin

class GalleryListView(LoginRequiredMixin,ListView):
    queryset = Gallery.objects.on_site().is_public()
    paginate_by = 20

class GalleryDetailView(LoginRequiredMixin, DetailView):
    queryset = Gallery.objects.on_site().is_public()

class PhotoListView(LoginRequiredMixin,ListView):
    queryset = Photo.objects.on_site().is_public()
    paginate_by = 20


class PhotoDetailView(LoginRequiredMixin,DetailView):
    queryset = Photo.objects.on_site().is_public()


class PhotoDateView(LoginRequiredMixin,object):
    queryset = Photo.objects.on_site().is_public()
    date_field = 'date_added'
    allow_empty = True