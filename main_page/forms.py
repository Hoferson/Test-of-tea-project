from django import forms
from .models import Contact_us_form

class Contact_us_form(forms.ModelForm):

    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'type': "text",
        'class': "email-bt",
        'placeholder': "Name",
        'name': "Name",}))
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'type': "text",
        'class': "email-bt",
        'placeholder': "Email",
        'name': "Email",}))
    phone = forms.CharField(max_length=16, widget=forms.TextInput(attrs={
        'type': "text",
        'class': "email-bt",
        'placeholder': "Phone",
        'name': "Phone",}))
    message = forms.CharField(max_length=2000, widget=forms.Textarea(attrs={
        'class': "massage-bt",
        'placeholder': "Massage",
        'rows': "5",
        'id': "comment",
        'name': "text",}))

    class Meta:
        model = Contact_us_form
        fields = ('name', 'email', 'phone', 'message')
