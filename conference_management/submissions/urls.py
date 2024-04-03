from django.urls import path
from . import views

urlpatterns = [
    path('', views.submit_paper, name='submit_paper'),
    path('c/<uuid:paper_id>/', views.chair_paper_details, name='chair_paper_details'),
    path('a/<uuid:paper_id>/', views.author_paper_details, name='author_paper_details'),
    path('r/<uuid:paper_id>/', views.reviewer_paper_details, name='reviewer_paper_details'),
    path('r/review-paper/<uuid:paper_id>', views.review_paper, name='review_paper'),
    path('c/view_papers/', views.chair_view_papers, name='chair_view_papers'),
    path('c/assign-reviewers/', views.assign_reviewers, name='assign_reviewers'),
    path('c/accept-reject/', views.accept_reject, name='accept_reject'),
    path('c/view-comments/<uuid:paper_id>/', views.view_comments, name='view_comments'),
    path('c/accept-reject-paper/<uuid:paper_id>/', views.accept_reject_paper, name='accept_reject_paper'),
    path('c/assign-reviewers-to-paper/<uuid:paper_id>/', views.assign_reviewers_to_paper, name='assign_reviewers_to_paper'),
]

