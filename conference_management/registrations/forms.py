from django import forms
from .models import Attendee

class AttendeeForm(forms.ModelForm):
    class Meta:
        model = Attendee
        fields = ['first_name', 'last_name', 'email', 'organization']
