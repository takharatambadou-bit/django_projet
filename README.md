# Blog Django - Master 2 MICDA

Projet de création d'un blog avec le framework Django développé dans le cadre du cours "Langages et Frameworks Backend 2".

## 📋 Description

Ce projet est un blog fonctionnel développé avec Django qui permet de :
- Créer, modifier et supprimer des articles
- Afficher la liste des articles
- Lire le détail d'un article
- Gérer les fichiers statiques (CSS et images)
- Administrer le contenu via l'interface Django Admin

## 🚀 Installation

### Prérequis
- Python 3.8 ou supérieur
- pip (gestionnaire de paquets Python)
- Git

### Étapes d'installation

1. **Cloner le dépôt**
```bash
git clone <URL_DU_DEPOT>
cd blog_project
```

2. **Créer un environnement virtuel**
```bash
python -m venv venv
```

3. **Activer l'environnement virtuel**

Sur Windows :
```bash
venv\Scripts\activate
```

Sur macOS/Linux :
```bash
source venv/bin/activate
```

4. **Installer les dépendances**
```bash
pip install -r requirements.txt
```

5. **Effectuer les migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

6. **Créer un superutilisateur (administrateur)**
```bash
python manage.py createsuperuser
```
Suivez les instructions pour définir un nom d'utilisateur, email et mot de passe.

7. **Créer les dossiers pour les fichiers media**
```bash
mkdir media
mkdir media/articles
```

8. **Lancer le serveur de développement**
```bash
python manage.py runserver
```

Le site sera accessible à l'adresse : http://127.0.0.1:8000/

## 📁 Structure du projet

```
blog_project/
│
├── blog_project/              # Configuration principale du projet
│   ├── __init__.py
│   ├── settings.py           # Paramètres du projet
│   ├── urls.py               # URLs principales
│   ├── asgi.py
│   └── wsgi.py
│
├── blog_app/                  # Application blog
│   ├── migrations/           # Migrations de la base de données
│   ├── static/              # Fichiers statiques
│   │   └── css/
│   │       └── style.css    # Styles CSS
│   ├── templates/           # Templates HTML
│   │   └── blog/
│   │       ├── base.html
│   │       ├── article_list.html
│   │       ├── article_detail.html
│   │       ├── article_form.html
│   │       └── article_confirm_delete.html
│   ├── __init__.py
│   ├── admin.py             # Configuration de l'admin
│   ├── apps.py
│   ├── models.py            # Modèle Article
│   ├── urls.py              # URLs de l'application
│   └── views.py             # Class-Based Views
│
├── media/                    # Fichiers uploadés (images)
├── db.sqlite3               # Base de données SQLite
├── manage.py                # Script de gestion Django
├── requirements.txt         # Dépendances Python
├── .gitignore              # Fichiers à ignorer par Git
└── README.md               # Ce fichier
```

## 🎯 Fonctionnalités

### 1. Affichage des articles (ListView)
- URL : `/`
- Affiche la liste de tous les articles
- Pagination disponible (10 articles par page)

### 2. Détail d'un article (DetailView)
- URL : `/article/<id>/`
- Affiche le contenu complet d'un article avec son image

### 3. Création d'un article (CreateView)
- URL : `/article/nouveau/`
- Formulaire de création avec titre, auteur, contenu et image

### 4. Modification d'un article (UpdateView)
- URL : `/article/<id>/modifier/`
- Formulaire de modification d'un article existant

### 5. Suppression d'un article (DeleteView)
- URL : `/article/<id>/supprimer/`
- Confirmation avant suppression

### 6. Interface d'administration
- URL : `/admin/`
- Gestion complète des articles
- Interface personnalisée avec filtres et recherche

## 🗄️ Modèle de données

### Article
| Champ            | Type          | Description                    |
|------------------|---------------|--------------------------------|
| titre            | CharField     | Titre de l'article (200 car.)  |
| contenu          | TextField     | Corps de l'article             |
| date_publication | DateTimeField | Date et heure de publication   |
| auteur           | CharField     | Nom de l'auteur (100 car.)     |
| image            | ImageField    | Image illustrative (optionnel) |

## 🎨 Technologies utilisées

- **Framework** : Django 5.0
- **Base de données** : SQLite
- **Frontend** : HTML5, CSS3
- **Gestion des images** : Pillow
- **Architecture** : Class-Based Views (CBV)

## 📝 Utilisation

### Accéder à l'interface d'administration
1. Démarrez le serveur : `python manage.py runserver`
2. Accédez à : http://127.0.0.1:8000/admin/
3. Connectez-vous avec le superutilisateur créé
4. Gérez vos articles depuis l'interface

### Créer un article depuis le site
1. Accédez à la page d'accueil : http://127.0.0.1:8000/
2. Cliquez sur "Nouvel Article"
3. Remplissez le formulaire
4. Cliquez sur "Créer"

## 🧪 Tests

Pour tester les fonctionnalités CRUD :

1. Créez plusieurs articles via l'interface ou l'admin
2. Vérifiez leur affichage sur la page d'accueil
3. Cliquez sur un article pour voir les détails
4. Modifiez un article
5. Supprimez un article (avec confirmation)
6. Vérifiez l'upload et l'affichage des images

## 📤 Déploiement sur GitHub

```bash
# Initialiser Git (si pas déjà fait)
git init

# Ajouter tous les fichiers
git add .

# Créer le premier commit
git commit -m "Initial commit - Blog Django projet"

# Ajouter le dépôt distant
git remote add origin <URL_DE_VOTRE_DEPOT>

# Pousser vers GitHub
git push -u origin main
```

## ⚠️ Notes importantes

- **SECRET_KEY** : En production, changez la clé secrète dans `settings.py`
- **DEBUG** : Mettez `DEBUG = False` en production
- **ALLOWED_HOSTS** : Configurez les hôtes autorisés en production
- **Base de données** : En production, utilisez PostgreSQL ou MySQL au lieu de SQLite
- **Fichiers media** : En production, utilisez un service de stockage comme AWS S3

## 👨‍💻 Auteur

Projet réalisé par [Votre Nom] dans le cadre du Master 2 MICDA - UNCHK

## 📅 Date de remise

**15 avril 2026 à 23h59**

## 📧 Contact

- Tuteur : Abdourahmane BALDÉ
- Email : abdourahmane.balde@unchk.edu.sn
- Email programme : master.micda@unchk.edu.sn

## 📜 Licence

Ce projet est réalisé dans un cadre éducatif.
