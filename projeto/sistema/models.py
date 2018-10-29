from django.db import models


class Aluno(models.Model):
    nome = models.CharField(max_length=100, blank=False)
    ra = models.PositiveIntegerField(default=123456, blank=False)
    trancou = models.BooleanField(null=True, blank=True, default=False)

    def __str__(self):
        return self.nome

