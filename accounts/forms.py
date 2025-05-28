from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, required = True)
    password = forms.CharField(widget=forms.PasswordInput)
    

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=150, required = True)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    
    