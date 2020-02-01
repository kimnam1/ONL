from django.urls import path

from date.views import OnlDV, OnlMonthLV, DateHomeView

urlpatterns = [
    path('', DateHomeView.as_view(), name='home'),
    path('<int:month>/', OnlMonthLV.as_view(), name='month LV'),
    path('<int:month>/<str:slug>/', OnlDV.as_view(), name='OnlDV'),
]