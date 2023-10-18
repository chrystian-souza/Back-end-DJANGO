

from django.shortcuts import render, HttpResponse
from .models import Products

def index(request):

    produtos = Products.objects.all()
    print(produtos)
    return render(request, 'pages/index.html', {'produtos': produtos})

