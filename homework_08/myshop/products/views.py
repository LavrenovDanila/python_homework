from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Product, Category

class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    paginate_by = 10  # Вы можете изменить это число, если нужно

    def get_queryset(self):
        return Product.objects.filter(available=True)

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'