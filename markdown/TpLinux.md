- Ouvrer un terminal puis afficher le répertoire courant
- Utiliser la commande `ls` sans option ni argument
- Créer un nouveau dossier nommé `Dossier1`
- Utiliser la commande `ls` sans option ni argument. Que remarquez-vous ?
    Dossier1 apparait comme premier dans la liste 
- Déplacez-vous dans le répertoire `./Dossier1`
- Vérifier que vous êtes bien arrivé !
- Puis créer un fichier vide nommé `fic1.txt` dans ce dossier.
- Revenir dans le répertoire `/workspaces/GpeMercredi`
- Utiliser la commande `ls -F` . Que remarquez-vous ?
    rajoute un /
- Réaliser deux copies de `fic1.txt` :
    - `fic2.txt` dans le répertoire `./Dossier1`
    - `fic3.txt` dans le répertoire `/workspaces/GpeMercredi`
- Renommer le fichier `fic1.txt` en `fichierNSI` . Commenter.
- Utiliser la commande `tree` pour contrôler le résultat.
- Utiliser la commande `cd ../` puis `pwd` . Que remarquez-vous ?
on se retrouve dans workspaces
- Supprimer le dossier `/workspaces/GpeMercredi/Dossier1` avec la commande `rmdir`. Commenter.
    on ne peut pas le supprimer car il n'est pas vide
- Utiliser la commande `rm -ir /workspaces/GpeMercredi/Dossier1` . Répondez y(yes) ou n(no).
- Afficher une aide sur la commande `rm` . Quel est le rôle de l’option `-i` ?
    prompt before every removal
- Créer les dossiers suivants :
    - `/workspaces/GpeMercredi/DA`
    - `/workspaces/GpeMercredi/DA/DB`
    - /workspaces/GpeMercredi/DA/DC`
- Utiliser la commande `tree` pour contrôler.
-  Se déplacer dans le dossier `/workspaces/GpeMercredi/DA/DC` et vérifier que vous êtes bien arrivé !
-  Utiliser la commande `cd ../../` et commenter.
-  Ouvrir le fichier `fic3.txt` avec l’éditeur `nano`
- Ecrire 3 fois la ligne *"J’aime NSI"*, 2 fois la ligne *"J’aime bien lire aussi"* et 1 fois *"Bye"*
-  Appuyer sur <kbd>Ctrl</kbd>+<kbd>x</kbd> pour demander à quitter l’éditeur et valider avec la touche <kbd>y</kbd>
-  Afficher les 4 premières lignes de `fic3.txt`
-  Afficher les 3 dernières lignes de `fic3.txt`
-  Afficher le contenu du fichier dans la console.
-  Rechercher le mot *"aime"* dans le fichier `fic3.txt` et commenter.
-  Appliquer la commande `uniq` à `fic3.txt` et commenter.
- Appliquer la commande `sort` à `fic3.txt` et commenter.
- Afficher le nombre de lignes et de mots dans `fic3.txt`
- Afficher tous les fichiers et dossiers cachés du répertoire `/workspaces/GpeMercredi6`


----------------
## correction
-pwd
