from django.db import models
from ckeditor.fields import RichTextField


class Pages(models.Model):
    title = models.CharField(verbose_name='Название страницы', max_length=100, default='')
    text = RichTextField(verbose_name='Текст')
    comments_status = models.BooleanField(verbose_name='Разрешить комментарии', default=False)
    show_status =  models.BooleanField(verbose_name='Показывать страницу', default=True)
    show_student_unification =  models.BooleanField(verbose_name='Показывать страницу в меню "Полезная информация', default=True)

    class Meta:
        verbose_name = 'Страницы'
        verbose_name_plural = 'Страницы'

    def __str__(self):
        return self.title
