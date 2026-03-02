from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Order, Order_product, Client, Category, Product, Manufacturer


class ProductListView(ListView):
    model = Product
    template_name = ''
    context_object_name = 'products'

    def get_queryset(self):
        queryset = Product.objects.all()
        category_id = self.request.GET.get('category')

        if category_id:
            queryset = queryset.filter(category_id=category_id)

        return queryset

class ProductDetailView (DetailView):
    model = Product
    template_name = 'storeapp/Product_Detail.html'
    context_object_name = 'products'



