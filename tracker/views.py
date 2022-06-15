from django.shortcuts import render
from .models import Job, Interview
from django.views.generic import View, CreateView
from django.urls import reverse, reverse_lazy
from django.db.models import Count
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
class JobListView(View):
    def get(self, request, *args, **kwargs):
        jobs = Job.objects.all().order_by('-date_applied')
        interviews = Job.objects.annotate(num_of_interviews=Count('interview'))
        
        context = {
            'jobs':jobs
        }

        return render(request, 'tracker/jobs.html', context=context)

class JobCreateView(SuccessMessageMixin, CreateView):
    model = Job
    fields=['position_name', 'company_name', 'location', 'applied_via']
    success_message = "Job added, Good luck"
    template_name: 'job_form.html'
    # returning redirect to job list after job is added
    def get_success_url(self):
        return reverse('job-list')