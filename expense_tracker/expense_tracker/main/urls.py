from django.urls import path
from expense_tracker.main import views

urlpatterns = [
    path('', views.home_page, name='home-page'),
]
