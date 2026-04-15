from django.db import models
from django.urls import reverse
from django.utils import timezone


class Article(models.Model):
    """
    Modèle représentant un article de blog.
    """
    titre = models.CharField(max_length=200, verbose_name="Titre")
    contenu = models.TextField(verbose_name="Contenu")
    BROUILLON = 'brouillon'
    PUBLIE = 'publie'
    STATUT_CHOICES = [
        (BROUILLON, 'Brouillon'),
        (PUBLIE, 'Publie'),
    ]
    statut = models.CharField(
        max_length=20,
        choices=STATUT_CHOICES,
        default=BROUILLON,
        verbose_name="Statut"
    )
    date_publication = models.DateTimeField(
        default=timezone.now,
        verbose_name="Date de publication"
    )
    auteur = models.CharField(max_length=100, verbose_name="Auteur")
    image = models.ImageField(
        upload_to='articles/',
        blank=True,
        null=True,
        verbose_name="Image"
    )
    
    class Meta:
        ordering = ['-date_publication']
        verbose_name = "Article"
        verbose_name_plural = "Articles"
    
    def __str__(self):
        return self.titre
    
    def get_absolute_url(self):
        """Retourne l'URL de détail de l'article"""
        return reverse('article-detail', kwargs={'pk': self.pk})
