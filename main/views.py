from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        'title': 'FLY-ALMATA',
        'content': 'главная страница - FLY_ALMATA',
 
    }
    
    return render(request, 'main/index.html', context)
    
    
def about(request):
    context = {
        'title': 'FLY ALMATA о нас',
        'content': 'Об FLY-ALMATA',
        # 'text_on_page':     
    }
    
    return render(request, 'main/about.html', context)


def flights(request):
    context = {
        'title': "flights",
        'content': 'you can see',
        
    }
    
    return render(request, 'main/flights.html',context)
# comment for checking git system
