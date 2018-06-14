from django.views import generic

from myapp import models, forms


class MyView(generic.TemplateView):
    template_name = "myapp/my_template.html"


class MyCreateView(generic.CreateView):
    model = models.MyModel
    form_class = forms.MyModelForm
    success_url = "/create_success/"