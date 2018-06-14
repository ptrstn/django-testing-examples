from django.shortcuts import render
from django.views import generic


class MyView(generic.TemplateView):
    template_name = "myapp/my_template.html"