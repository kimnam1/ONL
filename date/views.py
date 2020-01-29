from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView, TemplateView

from date.models import Onl

class DateHomeView(TemplateView):
    template_name = "home.html"

class OnlMonthLV(TemplateView):
    template_name = "date/onl_month_list.html"
    model = Onl

class OnlDV(DetailView):
    model = Onl

