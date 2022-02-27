from django.urls import path
from music_app.main import views

urlpatterns = [
    path('', views.home_page, name='home-page'),
    path('profile/create/', views.create_profile, name='create-profile'),

    path('profile/details/', views.profile_details, name='profile-details'),
    path('profile/delete/', views.delete_profile, name='delete-profile'),

    path('album/add/', views.create_album, name='create-album'),
    path('album/details/<str:pk>', views.album_details, name='album-details'),
    path('album/edit/<str:pk>', views.edit_album, name='edit-album'),
    path('album/delete/<str:pk>', views.delete_album, name='delete-album'),

]