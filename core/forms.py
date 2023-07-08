from django import forms


# Form to map with html input fields
class prompt(forms.Form):
    """ Form class for the write view """
    prompt = forms.CharField(max_length=100)