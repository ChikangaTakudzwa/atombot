from django import forms


# Form to map with html input fields
class MyForm(forms.Form):
    """ Form class for the write view """
    prompt = forms.CharField(label='Prompt', required=True)  # Remove the trailing comma here
