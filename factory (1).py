from datetime import datetime
from models import Task

class TaskFactory:
    """Design Pattern Factory pour centraliser la création des tâches."""
    _counter = 1

    @classmethod
    def create_task(cls, title: str, description: str, deadline_str: str, assignee: str) -> Task:
        # Transformation de la date (Logique isolée ici)
        date_obj = datetime.strptime(deadline_str, "%d/%m/%Y")
        task = Task(cls._counter, title, description, date_obj, assignee)
        cls._counter += 1
        return task