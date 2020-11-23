from django import forms
from upload.models import Picture


class PictureForm(forms.ModelForm):
    """
    Form for the image model
    """
    class Meta:
        model = Picture
        fields = ('title', 'image')
