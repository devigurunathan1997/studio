from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=50)
    date = forms.CharField(max_length=50)
    mobile = forms.CharField(max_length=10)
    address = forms.CharField(max_length=150)
    message = forms.CharField(max_length=250)
