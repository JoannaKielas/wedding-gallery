from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.views.generic import TemplateView
from braces.views import LoginRequiredMixin




class LoginRequiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)


class SomeSecretView(LoginRequiredMixin, TemplateView):
    template_name = "/photologue/gallerylist/"

   

    def get(self, request):
        return self.render_to_response({})


class PrivateView(PermissionsRequiredMixin, View):
    required_permissions = (
    'photologue.urls',
    )

    def get(self, request, *args, **kwargs):
        return HttpResponse('Permission granted!')
