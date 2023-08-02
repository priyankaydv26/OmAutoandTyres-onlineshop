from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product
from django.contrib.auth.decorators import login_required, permission_required


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'categories/category_list.html', {'categories': categories})

def product_list(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)
    return render(request, 'categories/product_list.html', {'category': category, 'products': products})

@login_required
def add_product(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    if request.method == 'POST':
        # Process the form data and create a new product in the category
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        available = request.POST.get('available', False)

        product = Product.objects.create(
            name=name,
            description=description,
            price=price,
            available=available,
            category=category
        )
        return redirect('admin:categories_category_change', object_id=category_id)

    return render(request, 'add_product.html', {'category': category})


@login_required
def update_product(request, category_id, product_id):
    category = get_object_or_404(Category, pk=category_id)
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        # Process the form data and update the product in the category
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        available = request.POST.get('available', False)

        product.name = name
        product.description = description
        product.price = price
        product.available = available
        product.save()

        return redirect('admin:categories_category_change', object_id=category_id)

    return render(request, 'update_product.html', {'category': category, 'product': product})


@login_required
@permission_required('categories.delete_product', raise_exception=True)
def remove_product(request, category_id, product_id):
    category = get_object_or_404(Category, pk=category_id)
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        # Delete the product from the category
        product.delete()
        return redirect('admin:categories_category_change', object_id=category_id)

    return render(request, 'remove_product.html', {'category': category, 'product': product})
