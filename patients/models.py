import uuid
from django.db import models

class Paciente(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11, unique=True)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome
