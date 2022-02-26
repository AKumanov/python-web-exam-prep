from .models import Profile


def get_profile():
    profile = Profile.objects.all()
    return profile[0] if profile else None


def calculate_budget_left(profile, expenses):
    budget = profile.budget
    return budget - sum(ex.price for ex in expenses)