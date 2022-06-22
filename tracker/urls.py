from django.contrib import admin
from django.urls import path
from .views import InterviewCreateView, JobCreateView, JobDetailView, JobListView, JobSearch, rejectedView

urlpatterns = [
    
    path('', JobListView.as_view(), name="job-list"),
    path('Jobs/add/', JobCreateView.as_view(), name='job-create'),
    path('Jobs/search', JobSearch.as_view(), name="job-search"),
    path('Jobs/<int:pk>/', JobDetailView.as_view(), name='job-detail'),
    path('Jobs/<int:pk>/AddInterview/', InterviewCreateView.as_view(), name="add-interview"),
    path('Jobs/<int:pk>/Rejected' , rejectedView, name='job-rejected'),
]
