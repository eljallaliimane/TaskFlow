"""
Pattern Strategy - Permet de changer d'algorithme de filtrage dynamiquement.
"""
from abc import ABC, abstractmethod
class FilterStrategy(ABC):
    """Interface Strategy pour les algorithmes de filtrage."""
    @abstractmethod
    def filter(self, tasks):
        """
        Filtre une liste de tâches selon un critère.

        Args:
            tasks (list[Task]): Liste des tâches à filtrer

        Returns:
            list[Task]: Liste des tâches filtrées
        """
        pass

class FilterByStatus(FilterStrategy):
    """Stratégie concrète: Filtre les tâches par statut."""

    def __init__(self, status):
        """
        Args:
            status (TaskStatus): Le statut à filtrer
        """
        self.status = status

    def filter(self, tasks):
        """Retourne les tâches ayant le statut spécifié."""
        return [
            t for t in tasks
            if t.status == self.status
        ]


class FilterByPriority(FilterStrategy):
    """Stratégie concrète: Filtre les tâches par priorité."""
    def __init__(self, priority):
        """
        Args:
            priority (str): La priorité à filtrer
        """
        self.priority = priority

    def filter(self, tasks):
        """Retourne les tâches ayant la priorité spécifiée."""
        return [
            t for t in tasks
            if t.priority == self.priority
        ]


class FilterByUser(FilterStrategy):
    """Stratégie concrète: Filtre les tâches par utilisateur assigné."""
    def __init__(self, user):
        """
        Args:
            user (User): L'utilisateur à filtrer
        """
        self.user = user

    def filter(self, tasks):
        """Retourne les tâches assignées à l'utilisateur spécifié."""
        return [
            t for t in tasks
            if t.assigned_user == self.user
        ]


class TaskFilterContext:
    """Contexte qui utilise une stratégie de filtrage."""
    def __init__(self, strategy):
        """
        Args:
             strategy (FilterStrategy): La stratégie de filtrage à utiliser
        """
        self.strategy = strategy

    def execute_filter(self, tasks):
        """
        Exécute le filtrage avec la stratégie actuelle.

        Args:
             tasks (list[Task]): Liste des tâches à filtrer

              Returns:
                   list[Task]: Liste des tâches filtrées
        """
        return self.strategy.filter(tasks)


