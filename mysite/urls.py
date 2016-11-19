from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib.auth.views import login, logout


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^photologue/', include('photologue_custom.urls',)),
    url(r'^photologue/', include('photologue.urls', namespace='photologue')),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^$', TemplateView.as_view(template_name="homepage.html"), name='homepage'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
