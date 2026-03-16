from django.urls import reverse_lazy

class CreateUpdateMixin:
    fields = "__all__"

class SuccessUrlProductMixin:
    success_url = reverse_lazy("product_list")

class SuccessUrlCategoryMixin:
    success_url = reverse_lazy("category_list")

class SuccessUrlManufacturerMixin:
    success_url = reverse_lazy("manufacturer_list")

class SuccessUrlOrderMixin:
    success_url = reverse_lazy("order_list")