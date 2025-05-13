from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('', views.dashboard, name='budget_dashboard'),
    path('setup/', views.setup, name='budget_setup'),

    # Summaries
    path('summary/', views.summary_list, name='budget_summary_list'),
    path('summary/<int:year>/', views.summary_year, name='budget_summary_year'),
    path('summary/<int:year>/<int:month>/', views.summary_month, name='budget_summary_month'),

    # Categories
    path('category/', include('budget.categories.urls')),

    # Budget
    path('budget/', views.budget_list, name='budget_budget_list'),
    path('budget/add/', views.budget_add, name='budget_budget_add'),
    path('budget/edit/<slug:slug>/', views.budget_edit, name='budget_budget_edit'),
    path('budget/delete/<slug:slug>/', views.budget_delete, name='budget_budget_delete'),

    # BudgetEstimates
    path('budget/<slug:budget_slug>/estimate/', views.estimate_list, name='budget_estimate_list'),
    path('budget/<slug:budget_slug>/estimate/add/', views.estimate_add, name='budget_estimate_add'),
    path('budget/<slug:budget_slug>/estimate/edit/<int:estimate_id>/', views.estimate_edit, name='budget_estimate_edit'),
    path('budget/<slug:budget_slug>/estimate/delete/<int:estimate_id>/', views.estimate_delete, name='budget_estimate_delete'),

    # Transaction
    path('transaction/', include('budget.transactions.urls')),
]