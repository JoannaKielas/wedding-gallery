from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login


urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^photologue/', include('photologue.urls', namespace='photologue')),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
    url(r'^$', TemplateView.as_view(template_name="homepage.html"), name='homepage'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
