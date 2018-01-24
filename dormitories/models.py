from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

from main.models import Employees


class DormitoriesImg(models.Model):
    title = models.CharField(verbose_name='Название', max_length=100, default='')
    img = models.FileField(verbose_name='Картинка')
    img_thumbnail = ImageSpecField(source='img', processors=[ResizeToFill(555, 470)], format='JPEG', options={'quality': 100})

    class Meta:
        verbose_name = 'Фотографии общежитий'
        verbose_name_plural = 'Фотографии общежитий'

    def __str__(self):
        return self.title


class Dormitories(models.Model):
    name = models.CharField(verbose_name='Название общежития', max_length=150, default='')
    description = models.TextField(verbose_name='Описание', max_length=2000, default='')
    location = models.CharField(verbose_name='Координаты', max_length=100, default='')
    images = models.ManyToManyField(DormitoriesImg, verbose_name='Фото общежитий')
    manager = models.ManyToManyField(Employees, verbose_name='Заведующая', related_name="manager")
    employees = models.ManyToManyField(Employees, verbose_name='Старостат', related_name="employees")

    class Meta:
        verbose_name = 'Общежития'
        verbose_name_plural = 'Общежития'

    def __str__(self):
        return self.name
