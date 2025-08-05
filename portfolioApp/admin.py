from django.contrib import admin
from .models import Project, ProjectImage, TechStack, ContactMessage, Testimonials, Certification

# Inline for adding multiple project images directly inside Project edit
class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

# Project admin
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'featured')
    list_filter = ('featured', 'created_at', 'tech_stack')
    search_fields = ('title',)
    inlines = [ProjectImageInline]
    filter_horizontal = ('tech_stack',)

# Tech stack admin
@admin.register(TechStack)
class TechStackAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# Contact messages admin
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email')

# Testimonials admin
@admin.register(Testimonials)
class TestimonialsAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'approved', 'created_at')
    list_filter = ('approved',)
    search_fields = ('name', 'designation', 'quote')
    list_editable = ('approved',)
    
@admin.register(Certification)
class CertificationsAdmin(admin.ModelAdmin):
    list_display = ('title', 'provider', "issued_date")
    search_fields = ('title', 'provider')