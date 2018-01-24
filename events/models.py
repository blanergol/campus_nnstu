from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class Events(models.Model):
    title = models.CharField(verbose_name='Название', max_length=150, default='')
    text = RichTextField(verbose_name='Описание', default='')
    location = models.CharField(verbose_name='Локация', max_length=100, default='')
    date = models.DateField(verbose_name='Дата', default=timezone.now)
    time_start = models.TimeField(verbose_name='Время начала', default=timezone.now)
    time_end = models.TimeField(verbose_name='Время конца', default=timezone.now)
    img = models.FileField(verbose_name='Картинка')
    img_thumbnail_short = ImageSpecField(source='img', processors=[ResizeToFill(380, 350)], format='JPEG', options={'quality': 100})
    img_thumbnail_full = ImageSpecField(source='img', processors=[ResizeToFill(774, 380)], format='JPEG', options={'quality': 100})

    class Meta:
        verbose_name = 'Мероприятия'
        verbose_name_plural = 'Мероприятия'

    def __str__(self):
        return self.title
