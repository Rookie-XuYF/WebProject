from django import forms
from django.contrib.auth.models import User



class UserLoginForm(forms.Form):
    username = forms.CharField(label='Username', widget=forms.TextInput(
        attrs={'placeholder': '输入用户名', 'id': 'user_name', 'class': 'form-control'}), max_length=50)
    password = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'placeholder': 'Enter your password', 'id': 'user_password', 'class': 'form-control'}), max_length=50,
                               required=True)

    class Meta:
        model = User
        fields = ['username', 'password']


