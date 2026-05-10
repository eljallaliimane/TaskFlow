# -*- coding: utf-8 -*-

import re
def is_valid_email(email: str) -> bool:
    """Vérifie si l'email est valide."""
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None
def is_strong_password(password: str) -> bool:
    """
    Vérifie si le mot de passe est fort :
    - au moins 8 caractères
    - contient majuscule, minuscule, chiffre et caractère spécial
    """
    if len(password) < 8:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'[0-9]', password):
        return False
    if not re.search(r'[\W_]', password):
        return False
    return True