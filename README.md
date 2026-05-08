# TaskFlow

## 📌 Description
TaskFlow est une application collaborative permettant de :
- Gérer des projets
- Créer et assigner des tâches
- Suivre leur état
- Notifier automatiquement les utilisateurs

## 🧱 Architecture
Architecture en couches (MVC simplifié) :
- **Controller** : API REST / UI
- **Service** : logique métier
- **Repository** : accès aux données
- **Model** : entités (User, Project, Task, Notification)

## 🧠 Design Patterns
- **Factory** : création centralisée des tâches
- **Observer** : notifications automatiques (Task → User + NotificationService)
- **Singleton** : NotificationService (instance unique)
- *(Optionnel)* Strategy : filtres de tâches

## 📂 Structure du projet
TaskFlow/
├── docs/
│   ├── diagrammes/
│   │   ├── use_case.png
│   │   ├── class_diagram.png
│   │   ├── sequence_creer_tache.png
│   │   ├── sequence_notification.png
│   │   ├── activite_cycle_tache.png
│   ├── rapport_conception.pdf
├── src/
│   ├── main/java/
│   │   ├── models/
│   │   ├── patterns/
│   │   ├── services/
│   │   ├── repository/
│   ├── test/
├── README.md
├── javadoc/
├── swagger.yam


## 🚀 API REST (Swagger)
- **Users**
  - `POST /users/register` → inscription
  - `POST /users/login` → connexion
- **Projects**
  - `POST /projects` → créer projet
  - `GET /projects/{id}` → détails projet
  - `DELETE /projects/{id}` → supprimer projet
- **Tasks**
  - `POST /tasks` → créer tâche
  - `PUT /tasks/{id}` → modifier tâche
  - `DELETE /tasks/{id}` → supprimer tâche
  - `PUT /tasks/{id}/assign` → assigner tâche
  - `PUT /tasks/{id}/status` → changer statut

## 📊 UML
- Use Case Diagram
- Class Diagram
- Sequence Diagram (Créer tâche, Notification)
- Activity Diagram (cycle de vie tâche)

## 🌿 Git Workflow
- `main` → stable
- `dev` → développement
- `feature/*` → fonctionnalités
- Exemple commit :
  - `feat: ajout création de tâche`
  - `fix: correction bug assignation`
  - `docs: ajout diagramme UML`

## 👥 Équipe
- Personne 1 : User Module
- Personne 2 : Project Module
- Personne 3 : Task Module
- Personne 4 : Notifications + Docs (Observer, Singleton, Swagger, README)
