from django.urls import path
from . import views

urlpatterns = [
    path('', views.submit_paper, name='submit_paper'),
    path('view-paper/<uuid:paper_id>/', views.paper_details, name='paper_details'),
]

