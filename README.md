# PROJET_APP_EMPLOI Nicolas CLEMENT

Projet fin de stage Outil de Recherche d'emploi à partir d'une analyse textuelle.

Organiser dans un dossier enfant templates les pages mapage et widget, les mots clés tirés du CV sont stockés dans le fichier wordscv.txt

1°) Lancer python new_token.py Cette requête vers l'API Pole Emploi Offres d'emplois génère un token actif 20 minutes pour le widget pole emploi. Coller manuellement ce jeton dans la page html du widget

2°) Lancer python app.py  
Consulter la page http://127.0.0.1:5000
et charger le CV d'un candidat au format .txt

3°) Lancer python server.py
Consulter la page http://localhost:8080/mapage.html

4°) En lisant attentivement chaque compétence, décocher les compétences qui ne sont pas encore acquise ou qui ne font pas partie de la recherche cible du candidat.
Depuis cette liste officielle des compétences "Etudes et développement informatique (M1805)", un mot clé cible par compétence est enregistré dans un dictionnaire.
Ces compétences "hard skills" sont toutes en forte tension sur le marché de l'emploi.

5°) Valider

L'application compare cette liste de mots clés et leur présence dans le CV du candidat.

Ceci donne une selection de mots clés pertinents pour le candidat. Mots clés auquels celui-ci n'aurait pas forcément spontanément pensé.

5°) Avec le résultat de la selection des mots clés, faire une recherche géographique sur la page pole-emploi avec l'api activée localement ou sur le web à l'adresse: devine.fr

Consulter les offres et postuler.
