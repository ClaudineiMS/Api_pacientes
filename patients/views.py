from rest_framework import viewsets
from .models import Paciente
from .serializers import PacienteSerializer
from rest_framework import generics

# View para listar todos os pacientes
class PacienteListView(generics.ListAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

# View para criar um novo paciente
class PacienteCreateView(generics.CreateAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

# View para recuperar os detalhes de um paciente específico
class PacienteDetailView(generics.RetrieveAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

# View para atualizar um paciente específico
class PacienteUpdateView(generics.UpdateAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

# View para deletar um paciente específico
class PacienteDeleteView(generics.DestroyAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer