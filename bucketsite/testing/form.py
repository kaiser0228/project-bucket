from django import forms

class NameForm(forms.Form):
    title = forms.CharField(label="Your name")
