from django.shortcuts import render
from django.views import generic
from .models import BizCategory


class BizCategoryView(generic.ListView):
    model = BizCategory
