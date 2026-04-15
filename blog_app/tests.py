from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.staticfiles import finders
from .models import Article
from django.utils import timezone


class ArticleModelTest(TestCase):
    """Tests pour le modèle Article"""
    
    def setUp(self):
        """Créer un article de test"""
        self.article = Article.objects.create(
            titre="Article de test",
            contenu="Contenu de test",
            auteur="Auteur Test",
            date_publication=timezone.now()
        )
    
    def test_article_creation(self):
        """Tester la création d'un article"""
        self.assertEqual(self.article.titre, "Article de test")
        self.assertEqual(self.article.auteur, "Auteur Test")
        self.assertTrue(isinstance(self.article, Article))
    
    def test_article_str(self):
        """Tester la représentation string de l'article"""
        self.assertEqual(str(self.article), "Article de test")
    
    def test_get_absolute_url(self):
        """Tester l'URL absolue de l'article"""
        url = self.article.get_absolute_url()
        self.assertEqual(url, f'/article/{self.article.pk}/')


class ArticleViewsTest(TestCase):
    """Tests pour les vues de l'application"""
    
    def setUp(self):
        """Initialiser le client de test et créer des articles"""
        self.client = Client()
        self.article1 = Article.objects.create(
            titre="Premier article",
            contenu="Contenu du premier article",
            auteur="Auteur 1"
        )
        self.article2 = Article.objects.create(
            titre="Deuxième article",
            contenu="Contenu du deuxième article",
            auteur="Auteur 2"
        )
    
    def test_article_list_view(self):
        """Tester la vue liste des articles"""
        response = self.client.get(reverse('article-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Premier article")
        self.assertContains(response, "Deuxième article")
        self.assertTemplateUsed(response, 'blog/article_list.html')
    
    def test_article_detail_view(self):
        """Tester la vue détail d'un article"""
        response = self.client.get(
            reverse('article-detail', kwargs={'pk': self.article1.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Premier article")
        self.assertTemplateUsed(response, 'blog/article_detail.html')
    
    def test_article_create_view(self):
        """Tester la vue de création d'article"""
        response = self.client.get(reverse('article-create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/article_form.html')
    
    def test_article_create_post(self):
        """Tester la création d'un article via POST"""
        data = {
            'titre': 'Nouvel article',
            'contenu': 'Contenu du nouvel article',
            'statut': Article.BROUILLON,
            'auteur': 'Nouvel auteur'
        }
        response = self.client.post(reverse('article-create'), data)
        self.assertEqual(response.status_code, 302)  # Redirection
        self.assertTrue(
            Article.objects.filter(titre='Nouvel article').exists()
        )
    
    def test_article_update_view(self):
        """Tester la vue de modification d'article"""
        response = self.client.get(
            reverse('article-update', kwargs={'pk': self.article1.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/article_form.html')

    def test_article_update_post(self):
        """Tester la modification d'un article via POST (titre, contenu, statut)"""
        response = self.client.post(
            reverse('article-update', kwargs={'pk': self.article1.pk}),
            {
                'titre': 'Article modifie',
                'contenu': 'Contenu modifie',
                'statut': Article.PUBLIE,
            }
        )
        self.assertEqual(response.status_code, 302)
        self.article1.refresh_from_db()
        self.assertEqual(self.article1.titre, 'Article modifie')
        self.assertEqual(self.article1.contenu, 'Contenu modifie')
        self.assertEqual(self.article1.statut, Article.PUBLIE)
    
    def test_article_delete_view(self):
        """Tester la vue de suppression d'article"""
        response = self.client.get(
            reverse('article-delete', kwargs={'pk': self.article1.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/article_confirm_delete.html')
    
    def test_article_delete_post(self):
        """Tester la suppression d'un article via POST"""
        article_id = self.article1.pk
        response = self.client.post(
            reverse('article-delete', kwargs={'pk': article_id})
        )
        self.assertEqual(response.status_code, 302)  # Redirection
        self.assertFalse(Article.objects.filter(pk=article_id).exists())

    def test_css_est_charge_depuis_base_template(self):
        """Verifier que le template de base charge le fichier CSS statique."""
        response = self.client.get(reverse('article-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '/static/css/style.css')

        css_path = finders.find('css/style.css')
        self.assertIsNotNone(css_path)

    def test_image_est_affichee_dans_les_templates(self):
        """Verifier que l'image d'un article est affichee en liste et en detail."""
        article_image = Article.objects.create(
            titre='Article image',
            contenu='Contenu avec image',
            auteur='Auteur image',
            image='articles/test-image.jpg',
        )

        list_response = self.client.get(reverse('article-list'))
        self.assertEqual(list_response.status_code, 200)
        self.assertContains(list_response, article_image.image.url)

        detail_response = self.client.get(
            reverse('article-detail', kwargs={'pk': article_image.pk})
        )
        self.assertEqual(detail_response.status_code, 200)
        self.assertContains(detail_response, article_image.image.url)
