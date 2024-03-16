from django.urls import path
from . import views

app_name = "news"
urlpatterns = [
    path("", views.scrape_articles, name="scrape_form"),
    path("articles/", views.article_list, name="article_list"),
]
