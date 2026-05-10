from models import User, Task
from services import ProjectService
from observers import NotificationService

# 1. Setup
service = ProjectService()
notif_system = NotificationService()

# 2. Création des utilisateurs
admin = User(1, "Anas", "ADMIN")
dev = User(2, "Sami", "MEMBER")

# 3. Créer un projet
mon_projet = service.create_project("AI_App", admin, "Build a smart bot")

if mon_projet:
    # Attacher le service de notification
    mon_projet.attach(notif_system)

    # 4. Ajouter des membres o les tâches
    mon_projet.add_member(dev)
    
    tache1 = Task(101, "Setup Database", "Pending", "2024-06-01")
    mon_projet.add_task(tache1)

    # 5. Tester l'update dial task
    tache1.update_status("Done")