from django.conf.urls import url
from django.views.generic import ListView, DetailView
from .models import Product

# The pattern right after "127.0.0.1:8000/products/"
urlpatterns = [
    # Calls a view for itself
    url(r'^$', ListView.as_view(queryset=Product.objects.all(),
                                template_name="products/products.html")),
    # pk = PrimaryKey (id) of each Product obj. pk is a digit (hence '\d')
    url(r'^(?P<pk>\d+)$', DetailView.as_view(model=Product,
                                             template_name="products/product.html")),
]