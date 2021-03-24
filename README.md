#Projet OurInsta : Delygram
***

## Table of contents
* [Fonctionnalités](#Fonctionnalités)
* [Structure du projet](#Structure-du-projet)


## Fonctionnalités
***
Notre projet intitulé Delaygram est un système d'information comparable au service Instagram.

Conformément au cahier des charges, notre application permet à un utilisateur de :
* Sauvegarder des images en y associant une description et des mots clés
* Retirer une image précédemment mise en ligne et modifier un post (seul l’utilisateur qui a chargé l’image peut faire ces actions). A noter que nous appelons post un ensemble d'une image, d'une description et de ses tags. Aussi des commentaires ainsi que des likes sont associés à chaque post.
* Parcourir les images en ligne (toutes les images puis seulement les images des abonnements de l'utilisateurs)
* Liker et unliker un post
* Poster des commentaires sur des posts
* Faire des recherches par mots clefs pour afficher des images
* Naviguer sur son profil et afficher le nombre d'images mis en ligne sur la plateforme et mis en ligne par l'utilisateur, la volumétrie est aussi accessible. Ainsi que le nombre d'images likées.

Mais nous avons aussi ajouté des fonctionnalités plus avancées en commençant par mettre en place un module d'authentification. Ainsi, chaque personne le désirant peut se créer un compte utilisateur. Puis, chaque utilisateur peu se connecter à la plateforme pour pouvoir poster des posts, des commentaires, liker des images, s'abonner à d'autres utilisateurs, naviguer sur son profil (voir ses abonnements, ces abonnés et ses posts). 

Des petits détails en plus :
* Limiter à l'affichage de 3 commentaires sur le fil des posts pour éviter un surchargement inutile de l'interface. Puis, si on le souhaite, il est possible d'afficher le reste des autres commentaires.
* Un utilisateur peut aussi afficher uniquement les posts des utilisateurs auxquels il est abonné en cliquant sur l'onglet "Mon Réseau" dans la tab bar de la page d'accueil
* 

## Structure du projet
***
(Résumé de la structure générale puis contenu des différents fichiers)

### Fichier style

#### index.css
 Fichier css dans lequel la mise en page d'éléments est réalisée. Que ce soit des classes ou des identifiants css.

###Fichier python

#### models.py
Fichier dans lequel les différentes classes de la base de données sont déclarés avec tous leurs attributs. Nous avons 5 classes : Follow, User, Post, Comment, PostLike. On définit également des propriétés sur chaque classe, qui sont en fait des fonctions et nous permette de définir des méthodes qu'on peut appliquer sur chaque élément de la base de données.



#### app.py
C'est le fichier principal de notre serveur, l'éxecution d'app.py commence par créer la database si elle n'existe pas, puis elle va définir toutes les fonctions qui sont utilisées par notre serveur. Les @ avant chaque fonction permettent de paramétrer la fonction côté serveur, par ex : @app.route va definir l'url à partir de la racine où la fonction définie en dessous est appelée. C'est donc ici que sont programmées toutes les actions importantes comme poster/supprimer un post ou un commentaire, liker/unliker etc ...

### Les templates

#### layout.html.jinja2
C'est le template qui est réutilisé dans tous les autres, il contient la barre de navigation avec les différentes fonctionnalités de la navbar, et permet ainsi de l'afficher sur toutes les pages du site sans avoir à recopier le code

#### homepage.html.jinja2
Fichier qui correspond à la page d'accueil qui affiche les posts des utilisateurs dans l'ordre où ils ont été créés 

#### forms.html.jinja2

#### edit_post_form.html.jinja2 
Fichier correspondant à la vue permettant de créer un pôst, on affiche simplement un formulaire avec toutes les informations que l'utilisateur doit remplir pour poster une image

#### profile.html.jinja2
Fichier correspondant à la page du profil de l'utilisateur. ELle est accessible uniquement pour les utilisateurs connectés. Dans cette page est affiché le tableau de bord de l'utilisateurs, ses followers, ses followed et ses posts mis en ligne.

#### signup.html.jinja2 et login.html.jinja2 
Fichier au travers desquels il est possible de s'inscrire et de se connecter et ainsi avoir accès aux fonctionnalités d'un utilisateur de la plateforme. Dans ces fichiers des formulaires permettent de rentrer les information nécéssaires pour respectivement créer un utilisateur dans la base de données et de s'authentifier.
