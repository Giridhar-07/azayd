from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from django.contrib import messages
from .models import Service, JobPosting, TeamMember, ContactMessage
from .forms import ContactForm

class HomeView(ListView):
    template_name = 'website/home.html'
    queryset = Service.objects.all()[:3]
    context_object_name = 'services'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['team_members'] = TeamMember.objects.filter(is_active=True)[:4]
        return context

class ServiceListView(ListView):
    template_name = 'website/services.html'
    model = Service
    context_object_name = 'services'

class ServiceDetailView(DetailView):
    template_name = 'website/service_detail.html'
    model = Service
    context_object_name = 'service'

class AboutView(ListView):
    template_name = 'website/about.html'
    model = TeamMember
    context_object_name = 'team_members'
    queryset = TeamMember.objects.filter(is_active=True)

class CareerListView(ListView):
    template_name = 'website/careers.html'
    model = JobPosting
    context_object_name = 'jobs'
    queryset = JobPosting.objects.filter(is_active=True)

class JobDetailView(DetailView):
    template_name = 'website/job_detail.html'
    model = JobPosting
    context_object_name = 'job'

class ContactView(CreateView):
    template_name = 'website/contact.html'
    form_class = ContactForm
    success_url = '/contact/thank-you/'

    def form_valid(self, form):
        messages.success(self.request, 'Thank you for your message. We will get back to you soon!')
        return super().form_valid(form)