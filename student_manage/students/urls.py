from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('add/', views.add_student, name='add_student'),
    path('delete/<int:student_id>/', views.delete_student, name='delete_student'),
    path('edit/<int:student_id>/', views.update_student, name='update_student'),
]
