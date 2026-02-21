from django.shortcuts import get_object_or_404, render

from .models import Product


def product_list(request):
    product = Product.objects.all()
    return render(request, "shop/product_list.html", {"products": product})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "shop/product_detail.html", {"product": product})
