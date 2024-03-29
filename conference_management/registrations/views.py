from django.shortcuts import render, redirect
from .models import Attendee
from .forms import AttendeeForm

# Create your views here.
def register_attendee(request):
    if request.method == 'POST':
        form = AttendeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registration_success')
    else:
        form = AttendeeForm()
    return render(request, 'registrations/register_attendee.html',{'form':form})
    
def registration_success(request):
    return render(request, 'registrations/registration_success.html')
