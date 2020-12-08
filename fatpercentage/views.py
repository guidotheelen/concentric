from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class NewFatpercentageView(LoginRequiredMixin, TemplateView):

    template_name = "new_fatpercentage.html"


class FatpercentageView(LoginRequiredMixin, TemplateView):

    template_name = "fatpercentage_stats.html"