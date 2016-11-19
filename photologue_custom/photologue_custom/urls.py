from django.conf.urls import url

from photologue_custom.views import CustomGalleryListView, CustomGalleryDetailView, CustomPhotoDetailView, \
     CustomPhotoListView, CustomGalleryArchiveIndexView, CustomGalleryYearArchiveView, CustomGalleryDateDetailView


urlpatterns = [
url(r'^gallerylist/$',
        CustomGalleryListView.as_view(),
        name='gallery-list'),


url(r'^gallery/(?P<slug>[\-\d\w]+)/$',
        CustomGalleryDetailView.as_view(),
        name='pl-gallery'),

url(r'^gallery/(?P<year>\d{4})/(?P<month>[0-9]{2})/(?P<day>\w{1,2})/(?P<slug>[\-\d\w]+)/$',
        CustomGalleryDateDetailView.as_view(month_format='%m'),
        name='gallery-detail'),

url(r'^gallery/$',
        CustomGalleryArchiveIndexView.as_view(),
        name='pl-gallery-archive'),

url(r'^photo/(?P<slug>[\-\d\w]+)/$',
        CustomPhotoDetailView.as_view(),
        name='pl-photo'),

url(r'^photolist/$',
        CustomPhotoListView.as_view(),
        name='photo-list'),


url(r'^gallery/(?P<year>\d{4})/$',
        CustomGalleryYearArchiveView.as_view(),
        name='pl-gallery-archive-year'),
]
