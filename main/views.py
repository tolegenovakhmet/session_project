from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        'title': 'Miras',
        'content': 'главная страница магазина - HOME',
        'list': ['first', 'second'],
        'dict': {'first': 2},
        'is_authenticated': False
    }
    
    return render(request, 'main/index.html', context)
    
    
def about(request):
    return HttpResponse('About page')

# comment for checking git system
