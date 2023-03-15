from django import forms
from django.contrib.auth.models import User
from .models import Profile, Screenshot


class ScreenshotForm(forms.ModelForm):
    """
    Upload a Screenshot
    """
    class Meta:
        model = Screenshot
        fields = ('image',)
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control-file'}),
        }
        labels = {
            'image': '',
        }


class ProfileUpdateForm(forms.ModelForm):
    """
    Update profile of a user
    """
    class Meta:
        model = Profile
        fields = ['age', 'city', 'bio']

    def __init__(self, *args, **kwargs):
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)
        # self.fields['username'].widget.attrs.update({'class': 'form-control'})
        # self.fields['last_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['city'].widget.attrs.update({'class': 'form-control'})
        self.fields['bio'].widget.attrs.update({'class': 'form-control'})

        # self.fields['avatar'].widget.attrs.update({'class': 'form-control-file'})
