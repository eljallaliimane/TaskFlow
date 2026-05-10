# -*- coding: utf-8 -*-

import hashlib
import secrets
def hash_password(password: str) -> str:
    """Retourne le hash SHA-256 du mot de passe."""
    return hashlib.sha256(password.encode()).hexdigest()
def generate_token(length: int = 32) -> str:
    """Génère un token sécurisé aléatoire."""
    return secrets.token_hex(length) 