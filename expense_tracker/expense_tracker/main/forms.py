from django import forms
from .models import Profile, Expense


class BoilerPlateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter first name..'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter last name..'
                }
            ),
        }


class CreateProfileForm(BoilerPlateProfileForm, forms.ModelForm):
    pass


class EditProfileForm(BoilerPlateProfileForm, forms.ModelForm):
    pass


class DeleteProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = []


class BoilerPlateExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Enter title..'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Enter short description..'
                }
            )
        }


class CreateExpenseForm(BoilerPlateExpenseForm, forms.ModelForm):
    pass


class EditExpenseForm(BoilerPlateExpenseForm, forms.ModelForm):
    pass


class DeleteExpenseForm(BoilerPlateExpenseForm, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BoilerPlateExpenseForm, self).__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
