from django.shortcuts import render

def catalog(request):
    return render(request, 'tickets/catolog.html')


def product(request):
    return render(request, 'tickets/product.html')