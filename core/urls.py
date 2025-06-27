from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('agregar/', views.agregar_estudiante, name='agregar_estudiante'),
    path('estudiante/<int:id>/', views.student_detail, name='student_detail'),
    path('exportar_excel/', views.exportar_excel, name='exportar_excel'),
]
