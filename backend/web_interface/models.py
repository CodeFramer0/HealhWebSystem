from django.db import models
from django.contrib.auth.models import User

class Organ(models.Model):

    name = models.CharField(verbose_name="Орган",max_length=128)
    
    class Meta:
        verbose_name = 'Орган'
        verbose_name_plural = 'Органы'
    def __str__(self):
        return self.name
    
class Complaint(models.Model):
    user = models.ForeignKey(User,related_name='users',
                             verbose_name='Пациент',
        on_delete=models.CASCADE,
    )
    organ = models.ForeignKey(Organ,
                                 related_name='Organs',
                                 on_delete=models.CASCADE,
                                 verbose_name='Орган',
                                 )
    title = models.CharField(verbose_name="Название",max_length=512)
    description = models.CharField(verbose_name='Описание',max_length=1024)
    date = models.DateField(verbose_name='Дата')
    
    class Meta:
        verbose_name = 'Жалоба'
        verbose_name_plural = 'Жалобы'
    def __str__(self):
        return self.title
    
