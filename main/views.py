from django.shortcuts import render

from .models import Slider, Employees, Contact, Leadership, StudentCouncil, Newspaper
from articles.models import Articles
from students.models import Students
from settings.models import Settings
from vr.models import Issues
from pages.models import Pages
from events.models import Events
from dormitories.models import Dormitories


# получение повторяющихся данных в отображении
def get_context_data(request):
    # обязательные данные
    settings = Settings.objects.first()
    pages = Pages.objects.all().filter(show_status=True, show_student_unification=False)
    pages_student_unification = Pages.objects.all().filter(show_status=True, show_student_unification=True)

    context_data = {'settings': settings, 'pages': pages, 'pages_student_unification':pages_student_unification}
    return context_data


def main(request):
    # загрузка обязательных данных
    context_data = get_context_data(request)

    employees = Employees.objects.filter(show_main_page_status=True, student_unification_status=False)
    articles = Articles.objects.all().order_by('-created_date')[:3]
    events = Events.objects.all().order_by('-date')[:4]
    slider = Slider.objects.all()

    employees_count = Employees.objects.count()
    students_count = Students.objects.count()
    events_count = Events.objects.count()
    issues_count = Issues.objects.count()
    hh = {'employees_count': employees_count, 'students_count': students_count, 'events_count': events_count, 'issues_count': issues_count}

    # вывод данных в отображении
    context_data.update({'events': events, 'articles': articles, 'employees': employees, 'hh': hh, 'slider': slider})
    return render(request, 'main/main.html', context_data)


def student_council(request):
    # загрузка обязательных данных
    context_data = get_context_data(request)

    student_council = StudentCouncil.objects.all()
    student_council_dormitories = Dormitories.objects.all().order_by('id')

    # вывод данных в отображении
    context_data.update({'student_council': student_council, 'student_council_dormitories': student_council_dormitories})
    return render(request, 'main/student_council.html', context_data)


def leadership(request):
    # загрузка обязательных данных
    context_data = get_context_data(request)

    leadership = Leadership.objects.all()

    # вывод данных в отображении
    context_data.update({'leadership': leadership})
    return render(request, 'main/leadership.html', context_data)


def dormitories(request):
    # загрузка обязательных данных
    context_data = get_context_data(request)

    dormitories = Dormitories.objects.all().order_by('id')

    # вывод данных в отображении
    context_data.update({'dormitories': dormitories})
    return render(request, 'dormitories/main.html', context_data)


def contact(request):
    # загрузка обязательных данных
    context_data = get_context_data(request)

    contact = Contact.objects.first()

    # вывод данных в отображении
    context_data.update({'contact': contact})
    return render(request, 'main/contact.html', context_data)


def newspaper(request):
    # загрузка обязательных данных
    context_data = get_context_data(request)

    newspaper = Newspaper.objects.all().order_by('-id')

    # вывод данных в отображении
    context_data.update({'newspaper': newspaper})
    return render(request, 'main/newspaper.html', context_data)


def student_unification(request):
    # загрузка обязательных данных
    context_data = get_context_data(request)

    employees = Employees.objects.filter(student_unification_status=True)

    # вывод данных в отображении
    context_data.update({'employees': employees})
    return render(request, 'main/student_unification.html', context_data)
