from django.shortcuts import render
import pkg_resources
from .models import Job, Interview
from django.views.generic import View, CreateView
from django.urls import reverse, reverse_lazy
from django.db.models import Count, Q
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

class JobDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        job = Job.objects.get(pk=pk)
        interviews = Interview.objects.filter(job=job)

        context ={
            'job':job,
            'interviews':interviews
        }

        return render(request, 'tracker/job_detail.html', context)


class JobSearch(View):
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('query')
        job_list = Job.objects.filter(Q(position_name__icontains=query))

        context = {
            'job_list':job_list
        }

        return render(request, 'tracker/search.html', context)

class InterviewCreateView(SuccessMessageMixin, CreateView):
    model = Interview
    fields=['interview_date', 'interviewer', 'type', 'thoughts', ]
    success_message = "Interview added, Good luck"
    template_name: 'interview_form.html'

    
    def form_valid(self, form):
        form.instance.job_id = self.kwargs['pk']
        return super(InterviewCreateView, self).form_valid(form)

    # returning redirect to job list after job is added
    def get_success_url(self):
            return reverse('job-detail', args=[self.kwargs['pk']])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['prev_job'] = self.kwargs['pk']
        return context