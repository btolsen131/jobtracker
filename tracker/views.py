from django.shortcuts import render
from .models import Job, Interview
from django.views.generic import View, CreateView
from django.urls import reverse
from django.db.models import Count

# Create your views here.
class JobListView(View):
    def get(self, request, *args, **kwargs):
        jobs = Job.objects.all().order_by('-date_applied')
        interviews = Job.objects.annotate(num_of_interviews=Count('interview'))
        
        context = {
            'jobs':jobs
        }

        return render(request, 'tracker/jobs.html', context=context)

class JobCreateView(CreateView):
    model = Job
    fields=['position_name', 'company_name', 'location', 'applied_via']
    success_message = "Job added, Good luck"
    def form_valid(self, form):
        return super().form_valid(form)

    # returning redirect to job list after job is added
    def get_success_url(self):
        return reverse('job-list')