from django.shortcuts import render
from .models import Job, Interview
from django.views import View

# Create your views here.
class JobListView(View):
    def get(self, request, *args, **kwargs):
        jobs = Job.objects.all()
        
        context = {
            'jobs':jobs
        }

        return render(request, 'tracker/jobs.html', context=context)

