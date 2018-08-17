from django.conf.urls import url, include
from . import views  # import views.py which is in this same dir (.)

# Return views assigned to urls in "personal" (index/home page)
urlpatterns = [
    url(r'^$', views.index, name='index'),  # "127.0.0.1:8000/products/"
    url(r'^contact/$', views.contact, name='contact'), # "127.0.0.1:8000/personal/contacts/"
]
