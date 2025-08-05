from django.shortcuts import render
from django.views.generic import  ListView, DetailView, FormView, TemplateView
from .forms import ContactForm
from .models import Project, ContactMessage, Testimonials, Certification
from django.urls import reverse_lazy

# Create your views here.
class HomeView(TemplateView):
    template_name = 'portfolioApp/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured_projects'] = Project.objects.filter(featured=True)
        context['testimonials'] = Testimonials.objects.filter(approved=True)
        return context
    
class ProjectListView(ListView):
    model = Project
    template_name = "portfolioApp/projects_list.html"
    context_object_name = 'projects'
    
class ProjectDetailView(DetailView):
    model = Project
    template_name = 'portfolioApp/project_detail.html'
    context_object_name = 'project'
    
class ContactFormView(FormView):
    model = ContactMessage
    template_name = 'portfolioApp/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
# class FeaturedProjectListView(ListView):
#     model = Project
#     template_name = 'portfolioApp/home.html'
#     context_object_name = 'featured_projects'
    
#     def get_queryset(self):
#         return Project.objects.filter(featured=True)

class AboutView(TemplateView):
    template_name = 'portfolioApp/about.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['certifications'] = Certification.objects.all()
        return context
    