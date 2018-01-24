from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from main.views import get_context_data
from .models import Articles
from settings.models import Settings

def main(request):
    # загрузка обязательных данных
    context_data = get_context_data(request)

    settings = Settings.objects.all().first()

    articles = Articles.objects.all().order_by('-created_date')
    paginator = Paginator(articles, settings.count_articles)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    # вывод данных в отображении
    context_data.update({'articles': articles})
    return render(request, 'articles/main.html', context_data)


def full(request, pk):
    # загрузка обязательных данных
    context_data = get_context_data(request)

    article = get_object_or_404(Articles, pk=pk)

    # вывод данных в отображении
    context_data.update({'article': article})
    return render(request, 'articles/full.html', context_data)
