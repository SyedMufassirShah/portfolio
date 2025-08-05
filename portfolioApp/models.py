from django.db import models

# Create your models here.
class TechStack(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(unique=True, null=False, max_length=400)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    git_url = models.URLField(unique=True)
    tech_stack = models.ManyToManyField(TechStack)
    featured = models.BooleanField(default=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project_images/')

    def __str__(self):
        return f"Image for {self.project.title}"
    
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) 
    
    def __str__(self):
        return f"Message From {self.name}"   
    
    
class Testimonials(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    designation = models.CharField(max_length=200, blank=True)
    quote = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.name} - {self.designation or ''}".strip()
    
    
class Certification(models.Model):
    title = models.CharField(max_length=200)
    provider = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='certifications/', null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    issued_date = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.title} - {self.provider}"