from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from main.views import get_context_data
from .models import Events
from settings.models import Settings


def main(request):
    # загрузка обязательных данных
    context_data = get_context_data(request)

    settings = Settings.objects.all().first()

    events = Events.objects.all().order_by('-date')
    paginator = Paginator(events, settings.count_events)
    page = request.GET.get('page')
    try:
        events = paginator.page(page)
    except PageNotAnInteger:
        events = paginator.page(1)
    except EmptyPage:
        events = paginator.page(paginator.num_pages)

    # вывод данных в отображении
    context_data.update({'events': events})
    return render(request, 'events/main.html', context_data)


def full(request, pk):
    # загрузка обязательных данных
    context_data = get_context_data(request)

    event = get_object_or_404(Events, pk=pk)

    # вывод данных в отображении
    context_data.update({'event': event})
    return render(request, 'events/full.html', context_data)
