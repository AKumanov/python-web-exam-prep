from django.shortcuts import render, redirect
from .models import Profile, Album
from .forms import CreateProfileForm, CreateAlbumForm, EditAlbumForm, DeleteAlbumForm, \
    DeleteProfileForm


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None


def home_page(request):
    profile = get_profile()
    if not profile:
        return redirect('create-profile')
    else:
        albums = Album.objects.all()
        context = {
            'profile': profile,
            'albums': albums,
        }
    return render(request, 'home-with-profile.html', context)


def create_profile(request):
    form = CreateProfileForm()
    profile = get_profile()
    if profile:
        return redirect('home-page')
    else:
        if request.method == 'POST':
            form = CreateProfileForm(request.POST)
            if form.is_valid():
                print(form.cleaned_data)
                form.save()
                return redirect('home-page')

    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'home-no-profile.html', context)


def create_album(request):
    form = CreateAlbumForm
    if request.method == 'POST':
        form = CreateAlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home-page')
    context = {
        'form': form,
    }

    return render(request, 'add-album.html', context)


def album_details(request, pk):
    album = Album.objects.get(id=pk)
    context = {
        'album': album,
    }
    return render(request, 'album-details.html', context)


def edit_album(request, pk):
    album = Album.objects.get(id=pk)
    form = EditAlbumForm(instance=album)
    if request.method == 'POST':
        form = EditAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home-page')

    context = {
        'album': album,
        'form': form,
    }
    return render(request, 'edit-album.html', context)


def delete_album(request, pk):
    album = Album.objects.get(id=pk)
    if request.method == 'POST':
        form = DeleteAlbumForm(request.POST, instance=album)
        if form.is_valid():
            album.delete()
            return redirect('home-page')

    form = DeleteAlbumForm(instance=album)
    context = {
        'form': form,
        'album': album,
    }
    return render(request, 'delete-album.html', context)


def profile_details(request):
    profile = get_profile()
    number_of_albums = Album.objects.all().count()
    context = {
        'profile': profile,
        'number_of_albums': number_of_albums,
    }
    return render(request, 'profile-details.html', context)


def delete_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            profile.delete()
            Album.objects.all().delete()
            return redirect('home-page')

    form = DeleteProfileForm(instance=profile)
    context = {
        'form': form,
    }
    return render(request, 'profile-delete.html', context)
