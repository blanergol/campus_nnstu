from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField


class Issues(models.Model):
    employees = models.ForeignKey('main.Employees', verbose_name='Сотрудник', default='')
    name = models.CharField(verbose_name='ФИО', max_length=100, default='')
    email = models.EmailField(verbose_name='Email', max_length=100, default='')
    phone = models.CharField(verbose_name='Телефон', max_length=30, default='')
    who = models.CharField(verbose_name='Кто по отношению к НГТУ', max_length=100, default='')
    who_sub = models.CharField(verbose_name='Рубрика', max_length=300, default='')
    subject = models.CharField(verbose_name='Тема', max_length=200, default='')
    question = models.TextField(verbose_name='Вопрос', max_length=500, default='')
    answer = RichTextField(verbose_name='Ответ', max_length=2000)
    publication = models.BooleanField(verbose_name='Публикация вопроса', default=False)
    date = models.DateField(verbose_name='Дата вопроса', default=timezone.now)
    date_answer = models.DateField(verbose_name='Дата ответа', default=timezone.now)
    comments = models.BooleanField(verbose_name='Разрешить обсуждение вопроса', default=False)

    class Meta:
        verbose_name = 'Вопросы'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.subject
