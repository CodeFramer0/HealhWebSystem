from django.db import models


class Complaint(models.Model):
    title = models.CharField(verbose_name="Название")
    description = models.CharField(verbose_name='Описание')
    date = models.DateField(verbose_name='Дата')