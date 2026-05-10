# -*- coding: utf-8 -*-

from models.User import User, Role
class AuthService: 
#Service d'authentification qui gère l'inscription et la connexion des utilisateurs
    def __init__(self):
        self.users = []
    def register(self, username: str, password: str, role: Role = Role.MEMBER):
        """
        Inscrire un nouvel utilisateur avec hachage du mot de passe
        """
        if any(u.username == username for u in self.users):
            raise ValueError("Username already exists")
        user = User(username, password, role)
        self.users.append(user)
        return user
    def login(self, username: str, password: str): 
#Vérifie les identifiants et retourne l'utilisateur si correct
        for user in self.users:
            if user.username == username and user.verify_password(password):
                return f"Login successful: {user}"
        raise ValueError("Invalid credentials")