"""
Implémentation du pattern Observer.
permet de notifier les utilisateurs lors de chargements.
"""
from abc import ABC, abstractmethod
class Observer(ABC):
    """Interface Observer - Contrat pour recevoir des notifications."""
    @abstractmethod
    def update(self, message):
        pass

class User(Observer):
    def __init__(self, username):
        self.username = username

    def update(self, message):
        print(f"[NOTIF] {self.username}: {message}")

    def __str__(self):
        return self.username


