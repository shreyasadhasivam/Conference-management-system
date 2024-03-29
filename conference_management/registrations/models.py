from django.db import models

# Create your models here.
class Attendee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    organization = models.CharField(max_length=255)

    def __str__(self):
        """String for representing the Attendee object."""
        return f'{self.first_name} {self.last_name}'
    

class Registration(models.Model):
    """Model representing a registration for the conference."""
    attendee = models.ForeignKey(Attendee, on_delete=models.CASCADE)
    registration_date = models.DateTimeField(auto_now_add=True)
    # Add more fields as needed

    def __str__(self):
        """String for representing the Registration object."""
        return f'{self.attendee} - {self.registration_date}'