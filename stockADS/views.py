from django.shortcuts import render, HttpResponse
from .models import Products 

def index(request):

    produtos = Products.objects.all()
    print(produtos)
    return render(request, 'pages/index.html', {'produtos':produtos})

def product_detail(request, id):
    product = Products.objects.get(id=id)
    return render(request, 'pages/product_detail.html', {'product':product}) ######  {'product':product}) serve para registrar o produto para poder visualizar na tela

def add_product(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        name = request.POST.get('category')
        name = request.POST.get('picture')
        name = request.POST.get('price')
        name = request.POST.get('description')
        name = request.POST.get('qtd')
        name = request.POST.get('discount')


        pass 
    else:
        return render(request, 'pages/add-product.html')

    