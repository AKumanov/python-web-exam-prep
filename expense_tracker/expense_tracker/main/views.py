from django.shortcuts import render, redirect
from .models import Expense, Profile
from .common import get_profile

# Create your views here.
'''•	http://localhost:8000/ - home page
•	http://localhost:8000/create/ - create expense page
•	http://localhost:8000/edit/<id>/ - edit expense page
•	http://localhost:8000/delete/<id>/ - delete expense page
•	http://localhost:8000/profile/ - profile page
•	http://localhost:8000/profile/edit/ - profile edit page
•	http://localhost:8000/profile/delete/ - delete profile page
'''


def home_page(request):
    profile = get_profile()
    if profile:
        template = 'home-with-profile.html'
    else:
        template = 'home-no-profile.html'

    context = {

    }
    return render(request, template, context)
