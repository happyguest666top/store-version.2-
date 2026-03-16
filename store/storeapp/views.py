from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Product, Category, Manufacturer, Client, Order, Order_product
from django.db.models import Count
from .mixins import (CreateUpdateMixin, SuccessUrlProductMixin, SuccessUrlCategoryMixin, SuccessUrlManufacturerMixin, SuccessUrlOrderMixin)

class ProductListView(ListView):
    model = Product
    template_name = "storeapp/Product/Product_List.html"
    context_object_name = "products"

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.request.GET.get('category')
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        from .models import Category
        context['categories'] = Category.objects.all()
        return context

class ProductDetailView(DetailView):
    model = Product
    template_name = "storeapp/Product/Product_Detail.html"
    context_object_name = "product"

class ProductCreateView(CreateUpdateMixin, SuccessUrlProductMixin, CreateView):
    model = Product
    fields = "__all__"
    template_name = "storeapp/Product/Product_Create.html"
    success_url = reverse_lazy("product_list")

class ProductUpdateView(CreateUpdateMixin, SuccessUrlProductMixin, UpdateView):
    model = Product
    fields = "__all__"
    template_name = "storeapp/Product/Product_Update.html"
    success_url = reverse_lazy("product_list")

class ProductDeleteView(SuccessUrlProductMixin, DeleteView):
    model = Product
    template_name = "storeapp/Product/Product_Delete.html"
    success_url = reverse_lazy("product_list")

class CategoryListView(ListView):
    model = Category
    template_name = "storeapp/Category/Category_List.html"
    context_object_name = "categories"

class CategoryDetailView(DetailView):
    model = Category
    template_name = "storeapp/Category/Category_Detail.html"
    context_object_name = "category"

    def get_queryset(self):
        # Додаємо кількість продуктів у кожній категорії
        return Category.objects.annotate(product_count=Count('product'))

class CategoryCreateView(CreateUpdateMixin, SuccessUrlCategoryMixin, CreateView):
    model = Category
    fields = "__all__"
    template_name = "storeapp/Category/Category_Create.html"
    success_url = reverse_lazy("category_list")

class CategoryUpdateView(CreateUpdateMixin, SuccessUrlCategoryMixin, UpdateView):
    model = Category
    fields = "__all__"
    template_name = "storeapp/Category/Category_Update.html"
    success_url = reverse_lazy("category_list")

class CategoryDeleteView(SuccessUrlCategoryMixin, DeleteView):
    model = Category
    template_name = "storeapp/Category/Category_Delete.html"
    success_url = reverse_lazy("category_list")

class ManufacturerListView(ListView):
    model = Manufacturer
    template_name = "storeapp/Manufacturer/Manufacturer_List.html"
    context_object_name = "manufacturers"

class ManufacturerDetailView(DetailView):
    model = Manufacturer
    template_name = "storeapp/Manufacturer/Manufacturer_Detail.html"
    context_object_name = "manufacturer"

class ManufacturerCreateView(CreateUpdateMixin, SuccessUrlManufacturerMixin, CreateView):
    model = Manufacturer
    fields = "__all__"
    template_name = "storeapp/Manufacturer/Manufacturer_Create.html"
    success_url = reverse_lazy("manufacturer_list")

class ManufacturerUpdateView(CreateUpdateMixin, SuccessUrlManufacturerMixin, UpdateView):
    model = Manufacturer
    fields = "__all__"
    template_name = "storeapp/Manufacturer/Manufacturer_Update.html"
    success_url = reverse_lazy("manufacturer_list")

class ManufacturerDeleteView(SuccessUrlManufacturerMixin, DeleteView):
    model = Manufacturer
    template_name = "storeapp/Manufacturer/Manufacturer_Delete.html"
    success_url = reverse_lazy("manufacturer_list")

class OrderListView(ListView):
    model = Order
    template_name = "storeapp/Order/Order_List.html"
    context_object_name = "orders"

class OrderDetailView(DetailView):
    model = Order
    template_name = "storeapp/Order/Order_Detail.html"
    context_object_name = "order"

class OrderCreateView(CreateUpdateMixin, SuccessUrlOrderMixin, CreateView):
    model = Order
    fields = "__all__"
    template_name = "storeapp/Order/Order_Create.html"
    success_url = reverse_lazy("order_list")

class OrderUpdateView(CreateUpdateMixin, SuccessUrlOrderMixin, UpdateView):
    model = Order
    fields = "__all__"
    template_name = "storeapp/Order/Order_Update.html"
    success_url = reverse_lazy("order_list")

class OrderDeleteView(SuccessUrlOrderMixin, DeleteView):
    model = Order
    template_name = "storeapp/Order/Order_Delete.html"
    success_url = reverse_lazy("order_list")

class HomeView(TemplateView):
    template_name = "storeapp/home.html"
    succes_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured_products'] = Product.objects.all()[:10]
        return context

class CartView(ListView):
    template_name = "storeapp/cart.html"
    context_object_name = "cart_items"
    succes_url = reverse_lazy('cart')

    def get_queryset(self):
        return Order_product.objects.filter(order__client=self.request.user, order__status="incart")

class ProfileView(TemplateView):
    template_name = "storeapp/profile.html"
    succes_url = reverse_lazy('profile')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orders'] = Order.objects.filter(client=self.request.user).exclude(status='incart')
        return context

class AboutView(TemplateView):
    template_name = "storeapp/about.html"
    succes_url = reverse_lazy('about')


