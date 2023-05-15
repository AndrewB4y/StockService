from django.urls import path
from . import views

urlpatterns = [
    path('', views.StocksInfoView.as_view(), name='stock'),
]