# -*- coding: utf-8 -*-

import bcrypt #Librairie permettant le hache et la vérification des mdp de manière sécurisée
import uuid
from enum import Enum
class Role(Enum):
    """
    Énumération des rôles utilisateurs.
    """
    ADMIN = "ADMIN"
    MEMBER = "MEMBER"
class User:
    """
    Classe représentant un utilisateur.
    """
    def __init__(self, username: str, password: str, role: Role):
        self.id = str(uuid.uuid4())  # identifiant unique
        self.username = username
        # Hachage du mot de passe avec bcrypt
        self.password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        self.role = role
    def verify_password(self, password: str) -> bool:
        """
        Vérifie si le mot de passe fourni correspond au hash stocké.
        """
        return bcrypt.checkpw(password.encode(), self.password)
    def __repr__(self):
        return f"User({self.username}, {self.role.value})"