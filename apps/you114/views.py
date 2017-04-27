from django.shortcuts import render
from django.views.generic import TemplateView
from .models import BizCategory


class IndexView(TemplateView):
    template_name = 'you114/index.html'
