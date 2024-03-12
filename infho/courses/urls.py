from django.urls import path
from .views import CoursesListView, CourseDetailView, VacationCoursesListView, VacationCourseDetailView

urlpatterns = [
    #path("", StartingPageView.as_view(), name="starting-page"),
    path("alle/", CoursesListView.as_view(), name="course-page"),
    path("alle/<slug:slug>/", CourseDetailView.as_view(), name="course-detail-page"),
    path("Ferienkurse/", VacationCoursesListView.as_view(), name="vacation-course-page"),
    path("Ferienkurse/<slug:slug>/", VacationCourseDetailView.as_view(), name="vacation-course-detail-page"),
]
