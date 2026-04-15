# Instructions de déploiement et d'utilisation

## 🚀 Démarrage rapide

### 1. Configuration initiale

```bash
# Cloner le projet
git clone <URL_DU_DEPOT>
cd blog_project

# Créer et activer l'environnement virtuel
python -m venv venv

# Sur Windows
venv\Scripts\activate

# Sur macOS/Linux
source venv/bin/activate

# Installer les dépendances
pip install -r requirements.txt
```

### 2. Configuration de la base de données

```bash
# Créer les migrations
python manage.py makemigrations

# Appliquer les migrations
python manage.py migrate
```

### 3. Créer un superutilisateur

```bash
python manage.py createsuperuser
```

Renseignez :
- Nom d'utilisateur
- Adresse email
- Mot de passe (à saisir deux fois)

### 4. Créer les dossiers media

```bash
# Sur Windows
mkdir media
mkdir media\articles

# Sur macOS/Linux
mkdir -p media/articles
```

### 5. Lancer le serveur

```bash
python manage.py runserver
```

Le site est accessible sur : http://127.0.0.1:8000/

## 📋 Checklist avant remise

- [ ] Le code source est complet
- [ ] Le fichier README.md est à jour
- [ ] Le fichier requirements.txt contient toutes les dépendances
- [ ] Le fichier .gitignore est configuré
- [ ] Les migrations sont créées
- [ ] Les 5 Class-Based Views sont implémentées
- [ ] Les templates HTML sont tous créés
- [ ] Le fichier CSS est présent et fonctionnel
- [ ] L'interface d'administration est personnalisée
- [ ] Le modèle Article contient tous les champs requis
- [ ] Le dépôt GitHub est public
- [ ] Le lien GitHub est envoyé aux deux adresses email

## 🧪 Tester les fonctionnalités

### Test manuel complet

1. **Accueil (ListView)**
   - Accédez à http://127.0.0.1:8000/
   - Vérifiez que la liste des articles s'affiche
   - Si aucun article, créez-en un

2. **Création d'article (CreateView)**
   - Cliquez sur "Nouvel Article"
   - Remplissez le formulaire
   - Ajoutez une image
   - Cliquez sur "Créer"
   - Vérifiez la redirection vers le détail

3. **Détail d'article (DetailView)**
   - Cliquez sur un article dans la liste
   - Vérifiez que tout le contenu s'affiche
   - Vérifiez que l'image s'affiche correctement

4. **Modification d'article (UpdateView)**
   - Dans le détail d'un article, cliquez sur "Modifier"
   - Modifiez le titre ou le contenu
   - Enregistrez
   - Vérifiez que les modifications sont appliquées

5. **Suppression d'article (DeleteView)**
   - Dans le détail d'un article, cliquez sur "Supprimer"
   - Vérifiez que la page de confirmation s'affiche
   - Confirmez la suppression
   - Vérifiez que l'article n'apparaît plus dans la liste

6. **Interface d'administration**
   - Accédez à http://127.0.0.1:8000/admin/
   - Connectez-vous
   - Vérifiez que vous pouvez gérer les articles
   - Testez les filtres et la recherche

### Tests automatisés

```bash
python manage.py test
```

## 📤 Pousser sur GitHub

### Première fois

```bash
# Initialiser Git
git init

# Ajouter tous les fichiers
git add .

# Créer le premier commit
git commit -m "Initial commit - Projet Blog Django"

# Créer un dépôt sur GitHub (via l'interface web)
# Puis ajouter le remote

git remote add origin https://github.com/VOTRE_USERNAME/VOTRE_REPO.git

# Pousser le code
git branch -M main
git push -u origin main
```

### Mises à jour ultérieures

```bash
git add .
git commit -m "Description des modifications"
git push
```

## 📧 Remise du projet

### Vérifications finales

1. Le dépôt GitHub est **public**
2. Le README.md est visible et complet
3. Tout le code est présent
4. Le projet fonctionne après clonage

### Envoyer le lien

Envoyez le lien de votre dépôt GitHub aux adresses :
- abdourahmane.balde@unchk.edu.sn
- master.micda@unchk.edu.sn

**Format de l'email :**

```
Objet : [MICDA] Projet Blog Django - [VOTRE NOM]

Bonjour,

Veuillez trouver ci-dessous le lien vers mon projet Blog Django :

Lien GitHub : https://github.com/VOTRE_USERNAME/VOTRE_REPO

Cordialement,
[Votre Nom]
```

## ⚠️ Problèmes courants et solutions

### Le serveur ne démarre pas
```bash
# Vérifier que l'environnement virtuel est activé
# Réinstaller Django
pip install --upgrade django
```

### Les images ne s'affichent pas
```bash
# Vérifier que le dossier media existe
# Vérifier settings.py :
# MEDIA_URL = '/media/'
# MEDIA_ROOT = BASE_DIR / 'media'

# Vérifier urls.py :
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

### Erreur de migration
```bash
# Supprimer la base de données
rm db.sqlite3

# Supprimer les fichiers de migration (sauf __init__.py)
rm blog_app/migrations/0*.py

# Refaire les migrations
python manage.py makemigrations
python manage.py migrate
```

### Pillow ne s'installe pas
```bash
# Sur Windows, installer Visual C++ Build Tools
# Sur macOS : brew install libjpeg
# Sur Linux : sudo apt-get install python3-dev libjpeg-dev
pip install Pillow
```

## 🎯 Critères d'évaluation

Assurez-vous que votre projet respecte tous les critères :

✅ **Fonctionnalités (40%)**
- ListView fonctionnelle
- DetailView fonctionnelle
- CreateView fonctionnelle
- UpdateView fonctionnelle
- DeleteView fonctionnelle

✅ **Technique (30%)**
- Utilisation correcte des CBV
- Modèle Article complet
- URLs correctement configurées
- Templates bien structurés

✅ **Interface (20%)**
- CSS appliqué et fonctionnel
- Images affichées correctement
- Interface d'administration personnalisée
- Navigation intuitive

✅ **Documentation (10%)**
- README.md complet
- Code commenté
- Dépôt GitHub organisé

## 📚 Ressources utiles

- [Documentation Django](https://docs.djangoproject.com/)
- [Class-Based Views](https://docs.djangoproject.com/en/5.0/topics/class-based-views/)
- [Django Admin](https://docs.djangoproject.com/en/5.0/ref/contrib/admin/)
- [Django Static Files](https://docs.djangoproject.com/en/5.0/howto/static-files/)

Bon courage ! 🚀
