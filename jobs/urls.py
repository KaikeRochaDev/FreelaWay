from django.urls import path
from . import views

urlpatterns = [
    path('encontrar_jobs', views.encontrar_jobs, name='encontrar_jobs'),
    path('aceitar_job/<int:id>', views.aceitar_job, name='aceitar_job')
]


