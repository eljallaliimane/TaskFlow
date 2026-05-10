"""
Pattern Factory - Centralise la création des tâches.
Évite le couplage direct avec la classe Task.
"""
from task import Task
class TaskFactory:
    """Factory responsable de la création des objets Task."""
    @staticmethod
    def create_task(title, priority, user):
        """
        Crée et retourne une nouvelle instance de Task.

        Args:
            title (str): Titre de la tâche
            priority (str): Priorité de la tâche
            user (User): Utilisateur assigné

        Returns:
            Task: La nouvelle tâche créée
              """
        return Task(title, priority, user)