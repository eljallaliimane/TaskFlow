"""
Classe Task représentant une tâche du système.
Utilise NotificationService pour alerter les utilisateurs.
"""
from enums import TaskStatus
from notification_service import NotificationService

class Task:
    """Représente une tâche assignée à un utilisateur."""

    def __init__(self, title, priority, assigned_user):
        self.title = title
        self.status = TaskStatus.TODO
        self.priority = priority
        self.assigned_user = assigned_user

    def assign_user(self, user):
        self.assigned_user = user
        NotificationService().send_notification(
            user,
            f"Task assignée: {self.title}"
        )

    def change_status(self, new_status):
        self.status = new_status

    def update_task(self, new_title=None, new_priority=None):
        """
        Modifier une tâche existante - Nouvelle fonctionnalité.
        Déclenche une notification Observer.

        Args:
            new_title (str, optional): Nouveau titre
            new_priority (str, optional): Nouvelle priorité
        """
        if new_title:
            old_title = self.title
            self.title = new_title
            NotificationService().send_notification(
                self.assigned_user,
                f"Tâche modifiée: {old_title} → {new_title}"
            )
        if new_priority:
            self.priority = new_priority
            NotificationService().send_notification(
                self.assigned_user,
                f"Priorité changée pour {self.title}: {new_priority}"
            )

    def delete_task(self):
        """
        Supprimer une tâche - Nouvelle fonctionnalité.
        Déclenche une notification Observer avant suppression.
        """
        NotificationService().send_notification(
            self.assigned_user,
            f"Tâche supprimée: {self.title}"
        )

    def __str__(self):
     return (
            f"Tâche: {self.title} | "
            f"Status: {self.status.value} | "
            f"Priority: {self.priority} | "
            f"User: {self.assigned_user}"
        )
