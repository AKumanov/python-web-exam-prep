from django.contrib import admin
from .models import Expense, Profile

# Register your models here.
admin.site.register(Expense)
admin.site.register(Profile)