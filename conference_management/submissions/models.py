from django.db import models
from django.contrib.auth.models import User
import uuid

class Paper(models.Model):
    STATUS_CHOICES = (
        ('not_reviewed', 'Not Reviewed'),
        ('under_review', 'Under Review'),
        ('reviewed', 'Reviewed'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    )

    TRACKS = (
        ('track01', 'Track One'),
        ('track02', 'Track Two'),
        ('track03', 'Track Three')
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    abstract = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    submission_date = models.DateTimeField(auto_now_add=True)
    track = models.CharField(max_length=50, choices=TRACKS)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='not_reviewed')
    reviewer1 = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='reviewer1', null=True, blank=True)
    reviewer2 = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='reviewer2', null=True, blank=True)
    assigned = models.BooleanField(default=False)
    review1_status = models.BooleanField(default=False)
    review2_status = models.BooleanField(default=False)
    def __str__(self):
        return self.title

class Comment(models.Model):
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.reviewer.username} on {self.paper.title}"
