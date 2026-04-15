from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Article


class ArticleListView(ListView):
    """
    Vue pour afficher la liste de tous les articles.
    """
    model = Article
    template_name = 'blog/article_list.html'
    context_object_name = 'articles'
    paginate_by = 10  # Pagination optionnelle


class ArticleDetailView(DetailView):
    """
    Vue pour afficher le détail d'un article.
    """
    model = Article
    template_name = 'blog/article_detail.html'
    context_object_name = 'article'


class ArticleCreateView(CreateView):
    """
    Vue pour créer un nouvel article.
    """
    model = Article
    template_name = 'blog/article_form.html'
    fields = ['titre', 'contenu', 'statut', 'auteur', 'image']
    
    def form_valid(self, form):
        """
        Appelé lorsque le formulaire est valide.
        """
        return super().form_valid(form)


class ArticleUpdateView(UpdateView):
    """
    Vue pour modifier un article existant.
    """
    model = Article
    template_name = 'blog/article_form.html'
    fields = ['titre', 'contenu', 'statut']


class ArticleDeleteView(DeleteView):
    """
    Vue pour supprimer un article avec confirmation.
    """
    model = Article
    template_name = 'blog/article_confirm_delete.html'
    success_url = reverse_lazy('article-list')
    context_object_name = 'article'
