from django.db import models


class Inscription(models.Model):
    id = models.AutoField(primary_key = True)
    id_curso = models.IntegerField()
    id_usuario = models.CharField(max_length = 20);
    max_activity = models.IntegerField()

