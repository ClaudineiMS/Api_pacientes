from django.urls import path
from .views import (
    PacienteListView,
    PacienteCreateView,
    PacienteDetailView,
    PacienteUpdateView,
    PacienteDeleteView
)

urlpatterns = [
    path('pacientes/', PacienteListView.as_view(), name='paciente-list'),  # Lista todos os pacientes
    path('pacientes/novo/', PacienteCreateView.as_view(), name='paciente-create'),  # Cria um novo paciente
    path('pacientes/<uuid:pk>/', PacienteDetailView.as_view(), name='paciente-detail'),  # Detalha um paciente específico
    path('pacientes/<uuid:pk>/editar/', PacienteUpdateView.as_view(), name='paciente-update'),  # Atualiza um paciente específico
    path('pacientes/<uuid:pk>/deletar/', PacienteDeleteView.as_view(), name='paciente-delete'),  # Deleta um paciente específico
]
