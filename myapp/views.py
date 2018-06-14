from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import generic

from myapp import models, forms


class MyView(generic.TemplateView):
    template_name = "myapp/my_template.html"


class MyCreateView(generic.CreateView):
    model = models.MyModel
    form_class = forms.MyModelForm
    success_url = "/create_success/"


@method_decorator(login_required, name="dispatch")
class MyUpdateView(generic.UpdateView):
    model = models.MyModel
    form_class = forms.MyModelForm
    success_url = "/update_success/"
