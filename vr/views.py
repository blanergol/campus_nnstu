from django.shortcuts import render, HttpResponse, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist

from main.views import get_context_data
from .models import Issues
from main.models import Employees
import json


def issues(request):
    # обязательные данные
    context_data = get_context_data(request)

    employees = Employees.objects.filter(leadership_status=True, student_unification_status=False)

    # вывод данных в отображении
    context_data.update({'employees': employees})
    return render(request, 'vr/issues.html', context_data)


def answer(request):
    # обязательные данные
    context_data = get_context_data(request)

    issues = Issues.objects.all().filter(publication=True)

    # вывод данных в отображении
    context_data.update({'issues': issues})
    return render(request, 'vr/answer.html', context_data)


def answer_full(request, pk):
    # обязательные данные
    context_data = get_context_data(request)

    issue = get_object_or_404(Issues, pk=pk)

    # вывод данных в отображении
    context_data.update({'issue': issue})
    return render(request, 'vr/answer_full.html', context_data)


def new_issue(request):
    if request.POST and request.is_ajax:
        employees_id = request.POST.get('employees')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        who = request.POST.get('who')
        who_sub = request.POST.get('who_sub')
        subject = request.POST.get('subject')
        question = request.POST.get('question')

        try:
            employees = Employees.objects.get(id=employees_id)
            Issues.objects.create(employees=employees, name=name, email=email, phone=phone, who=who, subject=subject, question=question, who_sub=who_sub)
            data_response = {'status': 'success'}
        except ObjectDoesNotExist:
            data_response = {'status': 'fail'}
        return HttpResponse(json.dumps(data_response))


def search(request):
    # обязательные данные
    context_data = get_context_data(request)

    if request.POST:
        issue = request.POST.get('issue')

        issues = Issues.objects.filter(question__contains=issue)

        # вывод данных в отображении
        context_data.update({'issues': issues})
        return render(request, 'vr/answer.html', context_data)
