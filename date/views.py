
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView

from date.models import Onl

class DateHomeView(TemplateView):
    template_name = "home.html"

class OnlMonthLV(ListView):
    template_name = "date/onl_month_list.html"
    model = Onl

    # def get_queryset(self, request):
    #     month = request.GET.get('month', None)
    #     return Onl.objects.filter(month=month)


class OnlDV(DetailView):
    model = Onl
