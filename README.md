TaskFlow:Application de gestion de tâches collaboratives
=>Contexte
TaskFlow est une application collaborative permettant à plusieurs utilisateurs de créer, organiser et suivre l’avancement des tâches au sein d’un projet.  
Ce projet est réalisé dans le cadre du module Conception Logicielle à l’École Supérieure de Technologie de Ouarzazate.
=>Fonctionnalités
- Gestion des utilisateurs : inscription, connexion, rôles (admin, membre).
- Gestion des projets : création, modification, suppression, ajout de membres.
- Gestion des tâches : création, modification, suppression, attribution, statut (À faire, En cours, Terminée), échéances.
- Notifications simplifiées lors de l’assignation d’une tâche.
- Recherche et filtres par statut, responsable ou projet.
=>Technologies utilisées
- Langage : Python 
- Framework : FastAPI (API REST + Swagger intégré)
- Versionnement : Git & GitHub
- Documentation : Docstrings + Sphinx + Swagger UI
=>Structure du projet
TaskFlow/
│
├── docs/                  # Documentation et diagrammes UML
│   ├── diagrammes/
│   └── rapport_conception.pdf
│
├── src/
│   └── main/
│       └── python/
│           ├── models/    # Classes principales (User, Project, Task…)
│           ├── services/  # Logique métier
│           ├── patterns/  # Design patterns (Singleton, Observer, Factory…)
│           └── utils/     # Fonctions utilitaires
│
├── tests/                 # Tests unitaires
├── README.md              # Présentation du projet
├── requirements.txt       # Dépendances Python
└── swagger.yaml           # Endpoints API
=>Installation et exécution
1. Cloner le dépôt :bash
   git clone https://github.com/votre-groupe/taskflow.git
   cd taskflow
2. Créer un environnement virtuel :
   bash
   python -m venv venv
   venv\Scripts\activate      
3. Installer les dépendances :
   bash
   pip install -r requirements.txt
4. Lancer le serveur FastAPI :
   bash
   uvicorn main:app --reload
5. Accéder à l’API :
   - Documentation Swagger : http://127.0.0.1:8000/docs
   - Documentation ReDoc : http://127.0.0.1:8000/redoc
=>Équipe
Projet réalisé par un groupe de 4 étudiants.  
Chaque membre contribue via des branches Git et des commits réguliers.
=>Livrables
- Diagrammes UML (cas d’utilisation, classes, séquences, activités).
- Code Python structuré avec design patterns.
- Documentation technique (docstrings + Swagger).
- Dépôt GitHub avec historique clair.
- Soutenance orale avec démonstration.
