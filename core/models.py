from django.db import models


class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    local = models.CharField(max_length=200)
    data = models.DateField()
    horario = models.TimeField()
    categoria = models.CharField(max_length=100)
    vagas = models.IntegerField()

    def __str__(self):
        return self.titulo


class Presenca(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    nome_aluno = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nome_aluno


class Comentario(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    texto = models.TextField()

    def __str__(self):
        return self.nome