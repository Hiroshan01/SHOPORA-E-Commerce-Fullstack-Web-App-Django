from django.db.models import Q
from django.views.generic import ListView

from .models import Product


class ProductListView(ListView):
    model = Product
    template_name = "catalog/product_list.html"
    context_object_name = "products"
    ordering = ("-created_at", "id")
    paginate_by = 12

    def get_queryset(self):
        qs = Product.objects.filter(is_active=True)

        query = self.request.GET.get("q")
        sort = self.request.GET.get("sort")
        min_price = self.request.GET.get("min_price")
        max_price = self.request.GET.get("max_price")

        if query:
            qs = qs.filter(Q(name__icontains=query) | Q(description__icontains=query))
        if min_price:
            qs = qs.filter(price__gte=int(min_price))
        if max_price:
            qs = qs.filter(price__lte=int(max_price))
        if sort:
            qs = qs.order_by(sort)


        return qs
