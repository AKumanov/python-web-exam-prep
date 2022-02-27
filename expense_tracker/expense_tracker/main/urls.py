from django.urls import path
from expense_tracker.main import views

urlpatterns = [
    path('', views.home_page, name='home-with-profile'),


    path('profile/', views.profile, name='profile'),
    path('profile/create/', views.home_no_profile, name='create-profile'),
    path('profile/edit/', views.edit_profile, name='edit-profile'),
    path('profile/delete/', views.delete_profile, name='delete-profile'),


    path('expense/create/', views.create_expense, name='create-expense'),
    path('expense/edit/<str:pk>/', views.edit_expense, name='edit-expense'),
    path('expense/delete/<str:pk>/', views.delete_expense, name='delete-expense'),
]
