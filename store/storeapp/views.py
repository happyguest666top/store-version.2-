from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Product, Category, Manufacturer, Client, Order, Order_product

class ProductListView(ListView):
    model = Product
    template_name = "storeapp/Product/Product_List.html"
    context_object_name = "products"

class ProductDetailView(DetailView):
    model = Product
    template_name = "storeapp/Product/Product_Detail.html"
    context_object_name = "product"

class ProductCreateView(CreateView):
    model = Product
    fields = "__all__"
    template_name = "storeapp/Product/Product_Create.html"
    success_url = reverse_lazy("product_list")

class ProductUpdateView(UpdateView):
    model = Product
    fields = "__all__"
    template_name = "storeapp/Product/Product_Update.html"
    success_url = reverse_lazy("product_list")

class ProductDeleteView(DeleteView):
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

class CategoryCreateView(CreateView):
    model = Category
    fields = "__all__"
    template_name = "storeapp/Category/Category_Create.html"
    success_url = reverse_lazy("category_list")

class CategoryUpdateView(UpdateView):
    model = Category
    fields = "__all__"
    template_name = "storeapp/Category/Category_Update.html"
    success_url = reverse_lazy("category_list")

class CategoryDeleteView(DeleteView):
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

class ManufacturerCreateView(CreateView):
    model = Manufacturer
    fields = "__all__"
    template_name = "storeapp/Manufacturer/Manufacturer_Create.html"
    success_url = reverse_lazy("manufacturer_list")

class ManufacturerUpdateView(UpdateView):
    model = Manufacturer
    fields = "__all__"
    template_name = "storeapp/Manufacturer/Manufacturer_Update.html"
    success_url = reverse_lazy("manufacturer_list")

class ManufacturerDeleteView(DeleteView):
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

class OrderCreateView(CreateView):
    model = Order
    fields = "__all__"
    template_name = "storeapp/Order/Order_Create.html"
    success_url = reverse_lazy("order_list")

class OrderUpdateView(UpdateView):
    model = Order
    fields = "__all__"
    template_name = "storeapp/Order/Order_Update.html"
    success_url = reverse_lazy("order_list")

class OrderDeleteView(DeleteView):
    model = Order
    template_name = "storeapp/Order/Order_Delete.html"
    success_url = reverse_lazy("order_list")
