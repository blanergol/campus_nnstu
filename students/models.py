from django.db import models


class Students(models.Model):
    surname = models.CharField(verbose_name='Фамилия', max_length=100, default='')
    name = models.CharField(verbose_name='Имя', max_length=100, default='')
    middle_name = models.CharField(verbose_name='Отчество', max_length=100, default='')
    email = models.EmailField(verbose_name='Email', max_length=100, default='')
    password_sha512 = models.CharField(verbose_name='SHA512 пароля', max_length=200, default='')
    phone = models.CharField(verbose_name='Телефон', max_length=100, default='')
    institute = models.CharField(verbose_name='Институт', max_length=100, default='')
    group = models.CharField(verbose_name='Группа', max_length=20, default='')
    dormitory = models.IntegerField(verbose_name='Общежитие', default=1)
    room = models.CharField(verbose_name='Комната', max_length=20, default='')
    status = models.BooleanField(verbose_name='Данные студента проверены', default=False)

    class Meta:
        verbose_name = 'Студенты'
        verbose_name_plural = 'Студенты'

    def __str__(self):
        return self.surname
