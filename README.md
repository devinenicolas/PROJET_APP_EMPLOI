# PROJET_APP_EMPLOI Nicolas CLEMENT

Projet fin de stage Outil de Recherche d'emploi à partir d'une analyse textuelle.

Organiser dans un dossier enfant templates les pages mapage et widget

1°) Lancer python new_token pour générer un token pour le widget pole emploi. Coller manuellement ce jeton dans la page html du widget

2°) Lancer python app.py  
Consulter la page http://127.0.0.1:5000
et charger le CV d'un candidat au format .txt

3°) Lancer python server.py et décocher des compétences qui ne sont pas encore acquise ou qui ne font pas partie de la recherche actuelle du candidat.
Valider

L'application compare:
- Une selection de mots clés cibles pour le métier: Etudes et développement informatique (M1805), tirée de la nomenclature officielle de compétences.
- Avec leur présence dans le CV du candidat.
Ceici donne une selection de mots clés pertinents.

4°) Avec le résultat de la selection des mots clés, faire une recherche géographique sur la page pole-emploi avec l'api activée localement ou sur le web à l'adresse: devine.fr

Consulter les offres et postuler.
