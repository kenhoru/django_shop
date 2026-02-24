from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render

from .cart import Cart
from .models import Category, Product


def product_list(request):
    categories = Category.objects.annotate(items_count=Count("products"))
    product = Product.objects.all()
    cat_id = request.GET.get("category")
    current_category_id = int(cat_id) if cat_id else None
    if cat_id:
        product = product.filter(category_id=cat_id)
    query = request.GET.get("q")
    if query:
        product = product.filter(title__icontains=query)
    return render(
        request,
        "shop/product_list.html",
        {
            "products": product,
            "categories": categories,
            "current_category_id": current_category_id,
        },
    )


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "shop/product_detail.html", {"product": product})


def cart_detail(request):
    cart = Cart(request)
    return render(request, "shop/cart_detail.html", {"cart": cart})


def cart_add(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = Cart(request)
    cart.add(product=product)
    return redirect("cart_detail")


def cart_remove(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = Cart(request)
    cart.remove(product)
    return redirect("cart_detail")
