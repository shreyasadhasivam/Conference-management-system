# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    middle_initial = forms.CharField(max_length=1)
    last_name = forms.CharField(max_length=30)
    role = forms.ChoiceField(choices=[('chair', 'Chair'), ('author', 'Author'), ('reviewer', 'Reviewer')])
    country_region = forms.CharField(max_length=100)
    google_scholar_id = forms.CharField(max_length=100, required=False)
    semantic_scholar_id = forms.CharField(max_length=100, required=False)
    dblp_id = forms.CharField(max_length=100, required=False)
    orcid_id = forms.CharField(max_length=100, required=False)
    open_review_id = forms.CharField(max_length=100, required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'middle_initial', 'last_name', 'role', 'country_region', 'google_scholar_id', 'semantic_scholar_id', 'dblp_id', 'orcid_id', 'open_review_id']

class LoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)