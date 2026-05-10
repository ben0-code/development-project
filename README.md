# development-project
Gestion des Employés - Django CRUD
Description

Cette application est un système simple de gestion des employés développé avec Django.
Elle permet de :

Ajouter un employé
Modifier un employé
Supprimer un employé
Afficher la liste des employés

L’interface utilise TailwindCSS + DaisyUI pour le design.

Fonctionnalités
Ajouter un employé

Création d’un nouvel employé via un formulaire.

Modifier un employé

Modification des informations d’un employé existant.

Supprimer un employé

Suppression avec une confirmation JavaScript avant suppression.

Liste des employés

Affichage de tous les employés enregistrés dans la base de données.

Technologies utilisées
Python
Django
HTML
TailwindCSS
DaisyUI
SQLite
Structure du projet
employe/
│
├── migrations/
├── templates/
│   └── employe/
│       ├── base.html
│       ├── list.html
│       └── formulaire.html
│
├── forms.py
├── models.py
├── urls.py
├── views.py
└── admin.py
Installation
1. Cloner le projet
git clone <url-du-projet>
2. Créer un environnement virtuel
python -m venv env
3. Activer l’environnement virtuel
Windows
env\Scripts\activate
Mac/Linux
source env/bin/activate
Installer Django
pip install django
Effectuer les migrations
python manage.py makemigrations
python manage.py migrate
Lancer le serveur
python manage.py runserver
URLs principales
Fonction	URL
Liste des employés	/
Ajouter un employé	/Ajouter/
Modifier un employé	/Modifier/id/
Supprimer un employé	/Supprimer/id/


Auteur

Traore Massa Ben Ismael

Email: ben.traore@epitech.eu

Améliorations en cours
Authentification utilisateur
Recherche d’employés
Pagination
API REST avec Django REST Framework
Upload de photo de profil
Tableau de bord statistiques