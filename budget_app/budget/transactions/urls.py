from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.transaction_list, name='budget_transaction_list'),
    path('add/', views.transaction_add, name='budget_transaction_add'),
    path('edit/<int:transaction_id>/', views.transaction_edit, name='budget_transaction_edit'),
    path('delete/<int:transaction_id>/', views.transaction_delete, name='budget_transaction_delete'),
]