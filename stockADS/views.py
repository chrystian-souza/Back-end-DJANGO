

from django.shortcuts import render, HttpResponse
from .models import Products

def index(request):

    produtos = Products.objects.get(id=1)
    print(produtos)
    return render(request, 'pages/index.html', {'produtos': produtos})

