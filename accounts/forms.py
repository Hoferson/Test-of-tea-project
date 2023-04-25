from django import forms
from django.contrib.auth import get_user_model, authenticate
from Test_of_tea.settings import MANAGER_IND

User = get_user_model()

class RegistrationForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'manager_ind')

    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'type': "text",
        'class': "email-bt",
        'placeholder': "Userame",
        'name': "Name",}))
    password = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'type': "text",
        'class': "email-bt",
        'placeholder': "Password",
        'name': "Name",}))
    password2 = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'type': "text",
        'class': "email-bt",
        'placeholder': "Repeat password",
        'name': "Name",}))
    manager_ind = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'type': "text",
        'class': "email-bt",
        'placeholder': "Manager_indentificator",
        'name': "Name",}))
    

    def clean_password2(self):
        if self.cleaned_data['password'] == self.cleaned_data['password2'] and self.cleaned_data['manager_ind'] == MANAGER_IND:
            return self.cleaned_data['password']
        
        raise forms.ValidationError('Passwords do not match or wrong manager_ind')
    

class LoginForm(forms.Form):

    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'type': "text",
        'class': "email-bt",
        'placeholder': "Userame",
        'name': "Name",}))
    password = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'type': "text",
        'class': "email-bt",
        'placeholder': "Password",
        'name': "Name",}))
    
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)

            if not user or not user.check_password(password):
                raise forms.ValidationError('Username or password is incorrect')
            
        return super().clean()