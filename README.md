#Projet OurInsta : Delygram
***

## Table of contents
* [Fonctionnalités](#Fonctionnalités)
* [Structure du projet](#Structure-du-projet)


### Fonctionnalités
***
Notre projet intitulé Delygram est un système d'information comparable au service Instagram.

Conformément au cahier des charges, notre application permet à un utilisateur de :
* Sauvegarder des images en y associant une description et des mots clés
* Retirer une image précédemment mise en ligne et modifier un post (seul l’utilisateur qui a chargé l’image peut faire ces actions). A noter que nous appelons post un ensemble d'une image, d'une description et de ses tags. Aussi des commentaires ainsi que des likes sont associés à chaque post.
* Parcourir les images en ligne (toutes les images puis seulement les images des abonnements de l'utilisateurs)
* Liker et unliker un post
* Poster des commentaires sur des posts
* Faire des recherches par mots clefs pour afficher des images
* Naviguer sur son profil et afficher le nombre d'images mis en ligne sur la plateforme et mis en ligne par l'utilisateur, la volumétrie est aussi accessible. Ainsi que le nombre d'images likées.

Mais nous avons aussi ajouté des fonctionnalités plus avancées en commençant par mettre en place un module d'authentification. Ainsi, chaque personne le désirant peut se créer un compte utilisateur. Puis, chaque utilisateur peu se connecter à la plateforme pour pouvoir poster des posts, des commentaires, liker des images, s'abonner à d'autres utilisateurs, naviguer sur son profil (voir ses abonnements, ces abonnés et ses posts). Un utilisateur peut aussi afficher uniquement les posts de ses abonnés.

Des petits détails en plus :
* Limiter à l'affichage de 3 commentaires sur le fil des posts pour éviter un surchargement inutile de l'interface. Puis, si l'on le souhaite, il est possible d'afficher le reste des autres commentaires.
* 
* 

### Structure du projet
***
 (contenu des différents fichiers)
#### models.py
Fichier dans lequel les différentes classes de la base de données sont déclarés avec tous leurs attributs. Nous avons 5 classes : Follow, User, Post, Comment, PostLike. A noter qu'un certain nombre de fonctions sont définies dans la classe User.

#### index.css
 Fichier css dans lequel la mise en page d'éléments est réalisée. Que ce soit des classes ou des identifiants css.

#### app.py


#### homepage.html.jinja2
Fichier qui correspond à la page d'accueil qui affiche les posts des utilisateurs dans l'ordre où ils ont été créés 

#### profile.html.jinja2
Fichier correspondant à la page du profil de l'utilisateur. ELle est accessible uniquement pour les utilisateurs connectés. Dans cette page est affiché le tableau de bord de l'utilisateurs, ses followers, ses followed et ses posts mis en ligne.

