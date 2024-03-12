from django.views.generic import ListView
from django.views.generic import DetailView
from .models import Course, VacationCourse


# Create your views here.
class CoursesListView(ListView):
    template_name = "courses/all_courses.html"
    model = Course
    context_object_name = "all_courses"
    ordering = ["-date"]


class CourseDetailView(DetailView):
    model = Course
    template_name = "courses/course_detail.html"
    context_object_name = "course"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['course_tags'] = self.object.tags.all()
        return context

class VacationCoursesListView(ListView):
    template_name = "courses/all_vacation_courses.html"
    model = VacationCourse
    context_object_name = "all_courses"
    ordering = ["-date"]

class VacationCourseDetailView(DetailView):
    model = VacationCourse
    template_name = "courses/vacation_course_detail.html"
    context_object_name = "course"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['course_tags'] = self.object.tags.all()
        return context
