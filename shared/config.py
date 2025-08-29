from functools import lru_cache
import os

class Settings:
    users_service_url: str = os.getenv('USERS_SERVICE_URL', 'http://localhost:8001')
    tasks_service_url: str = os.getenv('TASKS_SERVICE_URL', 'http://localhost:8002')

@lru_cache
def get_settings() -> 'Settings':
    return Settings()
