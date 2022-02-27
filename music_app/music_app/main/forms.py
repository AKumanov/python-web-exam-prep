from .models import Profile, Album
from django import forms


class BoilerPlateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        labels = {
            'username': ' Username',
            'email': 'Email',
            'age': 'Age',

        }
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Username'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Email'
                }
            ),
            'age': forms.NumberInput(
                attrs={
                    'placeholder': 'Age'
                }
            )
        }


class CreateProfileForm(BoilerPlateProfileForm, forms.ModelForm):
    pass


class DeleteProfileForm(BoilerPlateProfileForm, forms.ModelForm):
    class Meta:
        model = Profile
        fields = []


class BoilerPlateAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        widgets = {
            'album_name': forms.TextInput(
                attrs={
                    'placeholder': 'Album Name'
                }
            ),
            'artist': forms.TextInput(
                attrs={
                    'placeholder': 'Artist'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Description'
                }
            ),
            'image_url': forms.URLInput(
                attrs={
                    'placeholder': 'Image URL'
                }
            ),
            'price': forms.NumberInput(
                attrs={
                    'placeholder': 'Price'
                }
            )
        }


class CreateAlbumForm(BoilerPlateAlbumForm, forms.ModelForm):
    pass


class EditAlbumForm(BoilerPlateAlbumForm, forms.ModelForm):
    pass


class DeleteAlbumForm(BoilerPlateAlbumForm, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BoilerPlateAlbumForm, self).__init__(*args, **kwargs)

        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False
