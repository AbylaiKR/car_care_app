from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic
from .models import car_brand


def index(request):
    return render(request, 'catalog/index.html')


class CarBrandListView(LoginRequiredMixin, generic.ListView):
    model = car_brand
    template_name = 'catalog/car_brand_list.html'


