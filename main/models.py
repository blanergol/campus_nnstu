from django.db import models
from ckeditor.fields import RichTextField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class Slider(models.Model):
    title = models.CharField(verbose_name='Заголовок слайдера', max_length=300, default='')
    description = models.CharField(verbose_name='Текст на слайде', max_length=500, default='')
    button_text = models.CharField(verbose_name='Текст на кнопке', max_length=100, default='')
    button_link = models.CharField(verbose_name='Ссылка на кнпоке (Напрмер: contact, без домена сайта)', max_length=200, default='')
    img = models.FileField(verbose_name='Фотография')
    photo_thumbnail = ImageSpecField(source='img', processors=[ResizeToFill(1920, 753)], format='JPEG', options={'quality': 100})

    class Meta:
        verbose_name = 'Слайдер'
        verbose_name_plural = 'Слайдер'

    def __str__(self):
        return self.description


class Employees(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=100, default='')
    post = models.CharField(verbose_name='Должность', max_length=100, blank=True)
    description = RichTextField(verbose_name='Описание обязанностей', max_length=3000, default='')
    address = models.CharField(verbose_name='Адрес', max_length=400, default='')
    email = models.EmailField(verbose_name='Email(можно не заполнять)', max_length=100, blank=True)
    vk = models.CharField(verbose_name='Ссылка на VK(можно не заполнять)', max_length=100, blank=True)
    phone = models.CharField(verbose_name='Телефон', max_length=20, blank=True)
    photo = models.FileField(verbose_name='Фото')
    photo_thumbnail = ImageSpecField(source='photo', processors=[ResizeToFill(270, 340)], format='JPEG', options={'quality': 100})
    show_main_page_status = models.BooleanField(verbose_name='Вывести на главную страницу', default=False)
    time_work = RichTextField(verbose_name='Приемные часы', max_length=300, blank=True)
    leadership_status = models.BooleanField(verbose_name='Руководство', default=False)
    student_unification_status = models.BooleanField(verbose_name='Студенческие объединения', default=False)

    class Meta:
        verbose_name = 'Сотрудники'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return self.name


class Newspaper(models.Model):
    title = models.CharField(verbose_name='Название(выпуск)', max_length=300)
    images = models.FileField(verbose_name='Картика')
    images_thumbnail = ImageSpecField(source='images', processors=[ResizeToFill(270, 340)], format='JPEG', options={'quality': 100})
    file = models.FileField(verbose_name='Файл', max_length=300)

    class Meta:
        verbose_name = 'Газета'
        verbose_name_plural = 'Газета'

    def __str__(self):
        return self.title


class StudentCouncil(models.Model):
    group = models.CharField(verbose_name='Группа', max_length=300)
    description = RichTextField(verbose_name='Описание')
    employees = models.ManyToManyField(Employees, verbose_name='Работники')

    class Meta:
        verbose_name = 'Страница: Студсовет студгородка'
        verbose_name_plural = 'Страница: Студсовет студгородка'

    def __str__(self):
        return self.group


class Leadership(models.Model):
    group = models.CharField(verbose_name='Группа', max_length=300)
    employees = models.ManyToManyField(Employees, verbose_name='Работники')

    class Meta:
        verbose_name = 'Страница: Руководство'
        verbose_name_plural = 'Страница: Руководство'

    def __str__(self):
        return self.group


class Contact(models.Model):
    location = models.CharField(verbose_name='Координаты карты', max_length=150)
    email_form = models.EmailField(verbose_name='Email формы обратной связи', max_length=100)
    address = RichTextField(verbose_name='Адрес', max_length=200)
    phone = RichTextField(verbose_name='Телефон', max_length=100)
    email = models.CharField(verbose_name='Email на страницу', max_length=100, default='')
    contact_leadership = RichTextField(verbose_name='Руководство', default='')
    contact_ssg = RichTextField(verbose_name='ССГ', default='')

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'
