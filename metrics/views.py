from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class MetricsView(TemplateView):

    template_name = "metrics.html"