from django import forms


class PictureForm(forms.Form):
    """
    Form for the image model
    """
    title = forms.CharField(max_length=200)
    image = forms.ImageField()
