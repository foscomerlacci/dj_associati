# -*- coding: utf-8 -*-

from django.db import models

from model_utils.models import TimeStampedModel


class Socio(models.Model):
    nome = models.CharField(max_length=30)
    cognome = models.CharField(max_length=30)
    discipline = models.ManyToManyField("Disciplina", blank=True)

    class Meta:
        verbose_name = 'socio'
        verbose_name_plural = 'soci'

    def __str__(self):
        return self.nome + " " + self.cognome


class Disciplina(models.Model):
    disciplina = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'disciplina'
        verbose_name_plural = 'discipline'

    def __str__(self):
        return self.disciplina



