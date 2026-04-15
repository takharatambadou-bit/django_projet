from django.contrib import admin
from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    """
    Configuration de l'interface d'administration pour le modèle Article.
    """
    list_display = ('titre', 'auteur', 'statut', 'date_publication')
    list_filter = ('date_publication', 'auteur', 'statut')
    search_fields = ('titre', 'contenu', 'auteur')
    date_hierarchy = 'date_publication'
    ordering = ('-date_publication',)
    
    fieldsets = (
        ('Informations principales', {
            'fields': ('titre', 'auteur', 'statut')
        }),
        ('Contenu', {
            'fields': ('contenu', 'image')
        }),
        ('Publication', {
            'fields': ('date_publication',)
        }),
    )
