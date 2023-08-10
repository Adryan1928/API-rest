from django.db import models

class Cliente(models.Model):
    sexo_choices = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('N', 'Null')
    )

    nome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=50)
    idade = models.IntegerField()
    sexo = models.CharField(max_length=1, choices=sexo_choices, default='N')

    def __str__(self):
        return self.nome