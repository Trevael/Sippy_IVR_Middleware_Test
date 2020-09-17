from django.urls import path
from rest_framework import routers

from api import views


urlpatterns = [
    path('transactions', views.TransactionsAPIView.as_view(), name='transactions'),
]
