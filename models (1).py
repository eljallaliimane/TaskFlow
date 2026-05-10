from enum import Enum
from datetime import datetime

class TaskStatus(Enum):
    """Statuts possibles pour une tâche (Principe KISS)"""
    TODO = "À faire"
    IN_PROGRESS = "En cours"
    DONE = "Terminée"

class Task:
    """Représente une tâche. (Responsabilité Unique - SOLID)"""
    def __init__(self, task_id: int, title: str, description: str, deadline: datetime, assignee: str):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.deadline = deadline
        self.assignee = assignee
        self.status = TaskStatus.TODO

    def __repr__(self):
        return f"Task(id={self.task_id}, title='{self.title}', status='{self.status.value}')"