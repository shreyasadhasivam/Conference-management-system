from django.shortcuts import render, redirect, get_object_or_404
from .models import Paper
from .forms import PaperForm

def submit_paper(request):
    if request.method == 'POST':
        form = PaperForm(request.POST)
        if form.is_valid():
            paper = form.save(commit=False)
            paper.author = request.user
            paper.status = 'not_reviewed'  
            paper.save()
            return redirect('dashboard')
    else:
        form = PaperForm()
    return render(request, 'submit_paper.html', {'form': form})

def paper_details(request, paper_id):
    paper = get_object_or_404(Paper, id=paper_id)
    return render(request, 'paper_details.html', {'paper': paper})