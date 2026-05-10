class NotificationObserver:
    """Interface pour les observateurs (Abstraction)"""
    def update(self, user: str, message: str):
        pass

class SimpleNotificationService(NotificationObserver):
    """Implémentation concrète du service de notification."""
    def update(self, user: str, message: str):
        print(f"🔔 [NOTIF] Salut {user}, {message}")