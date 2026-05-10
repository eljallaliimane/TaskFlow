""""
Enumeration  des statuts possible pour une tache.
Utilisée dans le cadre du pattern state implicite.
"""
from enum import Enum
class TaskStatus(Enum):
    """ Représente les différents états d'une tache."""
    TODO = "TODO"
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"
