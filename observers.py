from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, message: str):
        pass

class NotificationService(Observer):
    def update(self, message: str):
        print(f"🔔 [NOTIF]: {message}")