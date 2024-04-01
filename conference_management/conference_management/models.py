from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, choices=[('chair', 'Chair'), ('author', 'Author'), ('reviewer', 'Reviewer')])
    country_region = models.CharField(max_length=100)
    google_scholar_id = models.CharField(max_length=100, blank=True, null=True)
    semantic_scholar_id = models.CharField(max_length=100, blank=True, null=True)
    dblp_id = models.CharField(max_length=100, blank=True, null=True)
    orcid_id = models.CharField(max_length=100, blank=True, null=True)
    open_review_id = models.CharField(max_length=100, blank=True, null=True)
