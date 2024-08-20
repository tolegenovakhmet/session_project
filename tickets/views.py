from django.shortcuts import render

def catalog(request):
    return render(request, 'tickets/catolog.html')


def product(request):
    return render(request, 'tickets/product.html')

def cart(request):
    return render(request, 'tickets/cart.html')