from django.shortcuts import render
from django.views.generic import TemplateView
from .models import BizCategory


class IndexView(TemplateView):
    template_name = 'you114/index.html'
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['biz_categories'] = BizCategory.objects.all()
        return context


