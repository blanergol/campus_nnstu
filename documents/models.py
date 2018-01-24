from django.db import models


class Documents(models.Model):
    title = models.CharField(verbose_name='Название', max_length=200, default='')
    file = models.FileField(verbose_name='Файл', default='')

    class Meta:
        verbose_name = 'Файлы'
        verbose_name_plural = 'Файлы'

    def __str__(self):
        return self.title
