from django.views.generic.dates import ArchiveIndexView, DateDetailView, DayArchiveView, MonthArchiveView, \
    YearArchiveView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from photologue.models import Photo, Gallery
from photologue.views import GalleryDateView, PhotoDateView
from django.contrib.auth.mixins import LoginRequiredMixin


# Gallery views.
class CustomGalleryListView(LoginRequiredMixin, ListView):
    queryset = Gallery.objects.on_site().is_public()
    paginate_by = 20


class CustomGalleryDetailView(LoginRequiredMixin, DetailView):
    queryset = Gallery.objects.on_site().is_public()


class CustomGalleryDateView(LoginRequiredMixin, object):
    queryset = Gallery.objects.on_site().is_public()
    date_field = 'date_added'
    allow_empty = True


class CustomGalleryDateDetailView(LoginRequiredMixin, DateDetailView):
    pass


class CustomGalleryArchiveIndexView(LoginRequiredMixin, GalleryDateView, ArchiveIndexView):
    pass


class CustomGalleryDayArchiveView(LoginRequiredMixin, GalleryDateView, DayArchiveView):
    pass


class CustomGalleryMonthArchiveView(LoginRequiredMixin, GalleryDateView, MonthArchiveView):
    pass


class CustomGalleryYearArchiveView(LoginRequiredMixin, GalleryDateView, YearArchiveView):
    make_object_list = True

# Photo views.


class CustomPhotoListView(LoginRequiredMixin, ListView):
    queryset = Photo.objects.on_site().is_public()
    paginate_by = 20


class CustomPhotoDetailView(LoginRequiredMixin, DetailView):
    queryset = Photo.objects.on_site().is_public()


class CustomPhotoDateView(LoginRequiredMixin, object):
    queryset = Photo.objects.on_site().is_public()
    date_field = 'date_added'
    allow_empty = True


class CustomPhotoDateDetailView(LoginRequiredMixin, PhotoDateView, DateDetailView):
    pass


class CustomPhotoArchiveIndexView(LoginRequiredMixin, PhotoDateView, ArchiveIndexView):
    pass


class CustomPhotoDayArchiveView(LoginRequiredMixin, PhotoDateView, DayArchiveView):
    pass


class CustomPhotoMonthArchiveView(LoginRequiredMixin, PhotoDateView, MonthArchiveView):
    pass


class CustomPhotoYearArchiveView(LoginRequiredMixin, PhotoDateView, YearArchiveView):
    make_object_list = True






