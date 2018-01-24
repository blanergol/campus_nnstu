from django.shortcuts import render

from main.views import get_context_data
from .models import Documents


def main(request):
    # загрузка обязательных данных
    context_data = get_context_data(request)

    documents = Documents.objects.all()

    # вывод данных в отображении
    context_data.update({'documents': documents})
    return render(request, 'documents/main.html', context_data)
