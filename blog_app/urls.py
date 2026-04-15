from django.urls import path
from .views import (
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView,
    ArticleUpdateView,
    ArticleDeleteView
)

urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('article/nouveau/', ArticleCreateView.as_view(), name='article-create'),
    path('article/<int:pk>/modifier/', ArticleUpdateView.as_view(), name='article-update'),
    path('article/<int:pk>/supprimer/', ArticleDeleteView.as_view(), name='article-delete'),
]
