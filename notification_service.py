"""
Service de notification - pattern singleton
Garantit une seule instance pour gérer toutes les notifications.
"""
class NotificationService:
    """Singleton gérant l'envoi des notifications aux utilisateurs. """
    __instance = None

    def __new__(cls):
        """
        Crée ou retourne l'instance unique du service.

         Returns:
                NotificationService: L'instance unique
         """

        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def send_notification(self, user, message):
        """
        Envoie une notification à un utilisateur.

        Args:
             user (User): L'utilisateur destinataire
             message (str): Le message à envoyer
        """
        user.update(message)
