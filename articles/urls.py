from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.article_list, name="list"),
    url(r'^(?P<slug>[\w-]+)/$', views.article_detail, name="details"),
]
