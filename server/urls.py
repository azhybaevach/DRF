from django.urls import path
from .views import *


urlpatterns = [
    path('students/list', StudentListView.as_view()),
    path('students/create', StudentCreateView.as_view()),
    path('students/detail/<int:id>', StudentDetailView.as_view()),

]