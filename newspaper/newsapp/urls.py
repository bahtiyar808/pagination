from django.urls import path
# Импортируем созданное нами представление
from .views import NewsList, NewsDetail, NewsSearch, NewsCreate, ArticleList


urlpatterns = [
   path('news/', NewsList.as_view(), name = 'news_list'),
   path('articles/', ArticleList.as_view(), name = 'article_list'),
   path('<int:pk>', NewsDetail.as_view(), name = 'news_detail'),
   path('search/', NewsSearch.as_view(), name = 'news_search'),
   path('create/', NewsCreate.as_view(), name='news_create'),
]