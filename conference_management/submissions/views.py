from django.shortcuts import render, redirect, get_object_or_404
from .models import Paper, Comment
from .forms import PaperForm, AssignReviewersForm, ReviewPaperForm, AcceptRejectForm
from conference_management.models import UserProfile
from django.http import HttpResponse

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

def chair_view_papers(request):
    papers = Paper.objects.all()
    return render(request, 'chair_view_papers.html', {'papers': papers})

def author_paper_details(request, paper_id):
    paper = get_object_or_404(Paper, id=paper_id)
    return render(request, 'author_paper_details.html', {'paper': paper})

def reviewer_paper_details(request, paper_id):
    paper = get_object_or_404(Paper, id=paper_id)
    return render(request, 'reviewer_paper_details.html', {'paper': paper})

def chair_paper_details(request, paper_id):
    paper = get_object_or_404(Paper, id=paper_id)
    return render(request, 'chair_paper_details.html', {'paper': paper})

def assign_reviewers(request):
    papers = Paper.objects.filter(assigned=False)
    return render(request, 'assign_reviewers.html', {'papers': papers})

def assign_reviewers_to_paper(request, paper_id):
    paper = get_object_or_404(Paper, id=paper_id)
    form = AssignReviewersForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        reviewer1 = form.cleaned_data['reviewer1']
        reviewer2 = form.cleaned_data['reviewer2']
        paper.reviewer1 = reviewer1
        paper.reviewer2 = reviewer2
        paper.assigned = True
        paper.save()
        return redirect('assign_reviewers')
    return render(request, 'assign_reviewer_to_paper.html', {'form': form, 'paper': paper})

def review_paper(request, paper_id):
    paper = Paper.objects.get(pk=paper_id)
    form = ReviewPaperForm(request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
            comment = form.save(commit=False)
            comment.paper = paper
            comment.reviewer = request.user
            comment.save()
            if request.user == paper.reviewer1:
                paper.review1_status = True
            if request.user == paper.reviewer2:
                paper.review2_status = True
            
            if paper.review1_status and paper.review2_status:
                paper.status = 'reviewed'
            paper.save()
            
            return redirect('dashboard')  
            
    return render(request, 'review_paper.html', {'form': form, 'paper': paper})

    
def accept_reject(request):
    reviewed_papers = Paper.objects.filter(status='reviewed')
    return render(request, 'accept_reject.html', {'reviewed_papers': reviewed_papers})

def accept_reject_paper(request, paper_id):
    paper = get_object_or_404(Paper, pk=paper_id)
    form = AcceptRejectForm(request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
            status = form.cleaned_data['status']
            if status == 'accept':
                paper.status = 'accepted'
            elif status == 'reject':
                paper.status = 'rejected'
            paper.save()
            return redirect('some_success_url')  # Redirect to some success page after accept/reject
            
    return render(request, 'accept_reject_paper.html', {'form': form, 'paper': paper})

def view_comments(request, paper_id):
    paper = get_object_or_404(Paper, pk=paper_id)
    comments = Comment.objects.filter(paper=paper)
    return render(request, 'view_comments.html', {'paper': paper, 'comments': comments})