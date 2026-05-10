# -*- coding: utf-8 -*-

import logging
# Configuration du logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("app.log"),  # Sauvegarde dans un fichier
        logging.StreamHandler()          # Affiche dans la console
    ]
)

logger = logging.getLogger("AppLogger")
def log_info(message: str):
    logger.info(message)
def log_error(message: str):
    logger.error(message)
def log_debug(message: str):
    logger.debug(message)