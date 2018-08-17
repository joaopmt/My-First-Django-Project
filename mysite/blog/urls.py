from django.conf.urls import url
from django.views.generic import ListView, DetailView
from .models import Post

# The pattern right after "127.0.0.1:8000/blog/"
urlpatterns = [
    # Calls a view for itself
    url(r'^$', ListView.as_view(queryset=Post.objects.all().order_by("-date")[:25],
                                template_name="blog/blog.html")),
    # pk = PrimaryKey (id) of each Post obj. pk is a digit (hence '\d')
    url(r'^(?P<pk>\d+)$', DetailView.as_view(model=Post,
                                             template_name="blog/post.html")),
]
