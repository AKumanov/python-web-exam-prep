from .models import Profile


def get_profile():
    profile = Profile.objects.all()
    return profile if profile else None
