from django.contrib import admin
from django.urls import path
from .views import JobCreateView, JobListView

urlpatterns = [
    
    path('', JobListView.as_view(), name="job-list"),
    path('Jobs/add/', JobCreateView.as_view(), name='job-create'),
    
]
