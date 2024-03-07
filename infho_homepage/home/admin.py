from django.contrib import admin

# Register your models here.
from .models import BlogPost, InfoPost, Kurs

@admin.register(InfoPost)
class InfoPostAdmin(admin.ModelAdmin):

  fieldsets = [
        (
            None,
            {
                "fields": ["pub_date", "title", "title_image_path", "content_text"],
            },
        ),
        
    ]

  def save_model(self, request, obj, form, change):
    instance = form.save(commit=False)
    instance.author = request.user
    instance.save()
    form.save_m2m()
    return instance
    

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):

  fieldsets = [
        (
            None,
            {
                "fields": ["pub_date", "title", "title_image_path", "content_text"],
            },
        ),
        (
            "Erweitert",
            {
                "classes": ["collapse"],
                "fields": ["image_path_array"],
            },
        ),
        
    ]

  def save_model(self, request, obj, form, change):
    instance = form.save(commit=False)
    instance.author = request.user
    instance.save()
    form.save_m2m()
    return instance

@admin.register(Kurs)
class KursAdmin(admin.ModelAdmin):
    pass
    
