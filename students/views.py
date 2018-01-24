from django.shortcuts import render, get_object_or_404, HttpResponse, HttpResponseRedirect

from main.views import get_context_data
from .models import Students
from settings.models import Settings
from pages.models import Pages
import hashlib, json


def main(request, pk):
    # обязательные данные
    context_data = get_context_data(request)

    student = get_object_or_404(Students, pk=pk)

    # вывод данных в отображении
    context_data.update({'student': student})
    return render(request, 'students/main.html', context_data)


def auth(request):
    # обязательные данные
    context_data = get_context_data(request)

    return render(request, 'students/auth.html', context_data)


def reg(request):
    # обязательные данные
    context_data = get_context_data(request)

    return render(request, 'students/reg.html', context_data)


def auth_students(request):
    if request.POST and request.is_ajax:
        email = request.POST.get('email')
        password = request.POST.get('password').encode('utf-8')

        password_sha512_tmp = hashlib.sha512(password)
        password_sha512_tmp = password_sha512_tmp.hexdigest()

        try:
            student = Students.objects.get(email=email, password_sha512=password_sha512_tmp)
            request.session['email'] = student.email
            request.session['id'] = student.id
            request.session['logged'] = True

            data_response = {'status': 'success', 'redirect': '/students/' + str(student.id)}
        except Students.DoesNotExist:
            data_response = {'status': 'fail'}
        return HttpResponse(json.dumps(data_response))


def reg_students(request):
    if request.POST and request.is_ajax:
        surname = request.POST.get('surname')
        name = request.POST.get('name')
        middle_name = request.POST.get('middle_name')

        email = request.POST.get('email')
        password = request.POST.get('password').encode('utf-8')
        phone = request.POST.get('phone')

        institute = request.POST.get('institute')
        group = request.POST.get('group')
        dormitory = request.POST.get('dormitory')
        room = request.POST.get('room')

        password_sha512 = hashlib.sha512(password)
        password_sha512 = password_sha512.hexdigest()

        student_tmp = Students.objects.all().filter(email=email, phone=phone)

        if (len(student_tmp) > 0):
            data_response = {'status': 'fail'}
        else:
            Students.objects.create(surname=surname, name=name, middle_name=middle_name, email=email, password_sha512=password_sha512, phone=phone, institute=institute,
                                    group=group, dormitory=dormitory, room=room, status=0)

            student = Students.objects.get(email=email, password_sha512=password_sha512)

            if student.password_sha512 == password_sha512:
                request.session['email'] = student.email
                request.session['id'] = student.id
                request.session['logged'] = True

            data_response = {'status': 'success'}
        return HttpResponse(json.dumps(data_response))


def reg_mp_students(request):
    if request.POST and request.is_ajax:
        request.session['email_tmp'] = request.POST.get('email')
        request.session['surname_tmp'] = request.POST.get('surname')
        request.session['phone_tmp'] = request.POST.get('phone')

        data_response = {'status': 'success', 'redirect': '/students/reg'}
        return HttpResponse(json.dumps(data_response))


def logout_students(request):
    del request.session['email']
    del request.session['id']
    del request.session['logged']

    return HttpResponseRedirect('/')
