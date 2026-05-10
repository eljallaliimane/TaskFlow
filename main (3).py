from service import TaskManager
from observers import SimpleNotificationService
from models import TaskStatus

def run_demo():
    # Initialisation
    manager = TaskManager()
    notif_service = SimpleNotificationService()
    manager.register_observer(notif_service)

    print("--- 1. Création de tâches ---")
    t1 = manager.ajouter_tache("Faire l'UML", "Diagramme de séquence", "20/05/2026", "Personne 3")
    
    print("\n--- 2. Mise à jour du statut ---")
    manager.modifier_statut(t1.task_id, TaskStatus.IN_PROGRESS)
    print(f"État actuel : {t1}")

    print("\n--- 3. Recherche (Filtre) ---")
    resultat = manager.filtrer_par_responsable("Personne 3")
    print(f"Résultat pour Personne 3 ({len(resultat)} tâches trouvées) :")
    for task in resultat:
        print(f"-> {task}")

if __name__ == "__main__":
    run_demo()