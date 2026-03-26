# utils.py

import logging
import os
from datetime import datetime
from typing import List, Tuple

from api_service.config import Config

def get_current_datetime() -> str:
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def get_current_timestamp() -> int:
    return int(datetime.now().timestamp())

def create_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.propagate = False
    return logger

def get_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    return create_logger(name, level)

def get_config() -> Config:
    return Config()

def get_db_uri() -> str:
    return os.environ.get('DB_URI', 'sqlite:///api_service.db')

def get_secret_key() -> str:
    return os.environ.get('SECRET_KEY', 'default_secret_key')

def get_allowed_origins() -> List[str]:
    return os.environ.get('ALLOWED_ORIGINS', 'https://example.com').split(',')

def get_allowed_methods() -> List[str]:
    return os.environ.get('ALLOWED_METHODS', 'GET,POST,PUT,DELETE').split(',')

def get_max_age() -> int:
    return int(os.environ.get('MAX_AGE', 3600))

def get_cors_config() -> Tuple[str, List[str], int]:
    allowed_origins = get_allowed_origins()
    allowed_methods = get_allowed_methods()
    max_age = get_max_age()
    return allowed_origins, allowed_methods, max_age