from django.contrib import admin
from django.urls import path
from .views import JobCreateView, JobDetailView, JobListView, JobSearch

urlpatterns = [
    
    path('', JobListView.as_view(), name="job-list"),
    path('Jobs/add/', JobCreateView.as_view(), name='job-create'),
    path('Jobs/search', JobSearch.as_view(), name="job-search"),
    path('Jobs/<int:pk>/', JobDetailView.as_view(), name='job-detail'),
]
