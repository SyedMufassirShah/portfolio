from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('projects/', views.ProjectListView.as_view(), name='projects-list'),
    path('project/<int:pk>/', views.ProjectDetailView.as_view(), name='project-detail'),
    path('contact/', views.ContactFormView.as_view(), name='contact'),
    path('about/', views.AboutView.as_view(), name='about'),
]
