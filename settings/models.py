from django.db import models
from ckeditor.fields import RichTextField


class Settings(models.Model):
    title = models.CharField(verbose_name='Название сайта', max_length=200, default='')
    description = models.TextField(verbose_name='Описаие сайта', max_length=500, default='')
    phone = models.CharField(verbose_name='Номер телефона', max_length=50, default='')
    address = RichTextField(verbose_name='Адрес', max_length=200, default='')
    link_instagram = models.CharField(verbose_name='Ссылка на Instagram', max_length=200, default='')
    link_vk = models.CharField(verbose_name='Ссылка на VK', max_length=200, default='')
    link_youtube = models.CharField(verbose_name='Ссылка на YouTube', max_length=200, default='')
    description_short_about = models.TextField(verbose_name='Описание сайта в подвале', max_length=400, default='')
    description_newspaper = RichTextField(verbose_name='Описание раздела Газета', max_length=2000, default='')
    description_student_council_dormitories = RichTextField(verbose_name='Описание Старостата', max_length=2000, default='')
    rules_vr = RichTextField(verbose_name='Правила для приемной', default='')
    count_articles = models.IntegerField(verbose_name='Количество новостей на странице', default=6)
    count_events = models.IntegerField(verbose_name='Количество мероприятий на странице', default=6)
    enable_vr = models.BooleanField(verbose_name='Виртуальная приемная включена', default=True)
    enable_students = models.BooleanField(verbose_name='Авторизация/Регистрация включена', default=True)

    class Meta:
        verbose_name = 'Настройки'
        verbose_name_plural = 'Настройки'

    def __str__(self):
        return self.title
