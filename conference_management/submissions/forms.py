from django import forms
from .models import Paper, Comment
from conference_management.models import UserProfile, User

class PaperForm(forms.ModelForm):
    file = forms.FileField(label='Upload File')

    class Meta:
        model = Paper
        fields = ['title', 'abstract', 'track']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['file'].required = False

        

class AssignReviewersForm(forms.Form):
    reviewer1 = forms.ModelChoiceField(queryset=User.objects.filter(userprofile__role='reviewer'))
    reviewer2 = forms.ModelChoiceField(queryset=User.objects.filter(userprofile__role='reviewer'))

class ReviewPaperForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))

    class Meta:
        model = Comment
        fields = ['comment']

class AcceptRejectForm(forms.Form):
    CHOICES = [('accept', 'Accept'), ('reject', 'Reject')]
    status = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)