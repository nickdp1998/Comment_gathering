# Comment_gathering
Projet personnel pour aider un étudiant au doctorat.<br />
Le but de ce projet est d'automatiser la collecte d'avis sur certains sites.

# Guide d'utilisation 
Notes générales

    - Pour arrêter le programme, entrez 'STOP' au lieu d'entrer une recherche
    - Librairie utilisée : selenium
    - Installation nécessaire : ChromeDriver

Expedia

    - Expedia semble bloquer l'automatisation (avis inaccessible sans faire
      une vérification d'abord), donc il faut compléter le test de vérification
      manuellement. 

    - Il est important d'utiliser des URL de expedia.com, et non expedia.ca (ou
      tout autre nom de domaine)
       

Google Review

    - Il est déconseillé d'aller chercher un trop grand nombre de commentaires
      (> 1000) à cause des temps de chargement
      
TripAdvisor

    - Très peu développé et restrictif, les pages sont différentes selon les
      catégorie. Dans l'état actuel, le programme peut uniquement gérer les
      restaurant sur le site en français (https://fr.tripadvisor.ca/)
