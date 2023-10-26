from django.shortcuts import render, redirect
from .models import Products, Categorias 
from random import randint
from datetime import datetime

def index(request):

    produtos = Products.objects.all()
    print(produtos)
    return render(request, 'pages/index.html', {'produtos':produtos})

def product_detail(request, id):
    product = Products.objects.get(id=id)
    return render(request, 'pages/product_detail.html', {'product':product}) ######  {'product':product}) serve para registrar o produto para poder visualizar na tela

def delete_product(request, id):
    product = Products.objects.get(id=id)
    product.delete()
    return redirect('home')

def add_product(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        cod = randint(100, 10000)
        category = request.POST.get('category')
        picture = request.get('picture')
        price = request.POST.get('price')
        description = request.POST.get('description')
        qtd = request.POST.get('qtd')
        discount = request.POST.get('discount')
        created_at = datetime.now()
        in_stock = True

        Products.objects.create(
            name=name, cod=cod, category_id=category, picture=picture,
            price=price, description=description, qtd=qtd, discount=discount,
            created_at = created_at, in_stock=in_stock
        )

        return redirect('home')

    else:

        categories = Categorias.objects.all()
        return render(request, 'pages/add-product.html', {'categories': categories})

    