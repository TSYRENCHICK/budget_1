from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from app1.models import Article
from django.http import JsonResponse

@csrf_exempt
def index(request):
    if request.method == 'POST':
        if 'item_name' in request.POST:
            try:
                item_name = request.POST.get('item_name')
                second_item_name = request.POST.get('second_item_name')
                sum = request.POST.get('sum')
                date = request.POST.get('date')
                Article.objects.create(item_name=item_name, second_item_name=second_item_name, sum=sum, date=date)
                return JsonResponse({'success': True})  # Отправляем JSON-ответ об успешном добавлении
            except Exception as e:
                print(e)
                return JsonResponse({'success': False, 'error': str(e)})  # Отправляем JSON-ответ с ошибкой, если что-то пошло не так

    articles = Article.objects.all()
    return render(request, 'index.html', {'articles': articles})

@csrf_exempt
def edit_article(request):
    if request.method == 'POST':
        try:
            article_id = request.POST.get('article_id')
            item_name = request.POST.get('item_name')
            second_item_name = request.POST.get('second_item_name')
            sum = request.POST.get('sum')
            date = request.POST.get('date')
            article = Article.objects.get(pk=article_id)
            article.item_name = item_name
            article.second_item_name = second_item_name
            article.sum = sum
            article.date = date
            article.save()
            return JsonResponse({'success': True})
        except Exception as e:
            print(e)
            return JsonResponse({'success': False, 'error': str(e)})
