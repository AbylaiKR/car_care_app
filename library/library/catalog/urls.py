from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cars', views.CarBrandListView.as_view(), name='cars'),
]