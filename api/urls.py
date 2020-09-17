from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from api import views


urlpatterns = [
    path('', views.api_root),
    path('transactions/', views.TransactionsList.as_view(), name='transactions-list'),
    path('transactions/<int:pk>', views.TransactionDetail.as_view(), name='transaction-detail'),
    path('transactions/record/', views.TransactionCreate.as_view(), name='transaction-create'),
    path('transactions/record/<int:pk>', views.TransactionUpdate.as_view(), name='transaction-update'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
