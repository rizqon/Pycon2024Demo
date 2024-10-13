from logto import LogtoClient, LogtoConfig, Storage
from django.contrib.sessions.backends.db import SessionStore
from typing import Union
from django.conf import settings

session = SessionStore()

class SessionStorage(Storage):
    def get(self, key: str) -> Union[str, None]:
        return session.get(key, None)

    def set(self, key: str, value: Union[str, None]) -> None:
        session[key] = value

    def delete(self, key: str) -> None:
        session.pop(key, None)

client = LogtoClient(
    LogtoConfig(
        endpoint=settings.LOGTO['app_endpoint'],
        appId=settings.LOGTO['app_id'],
        appSecret=settings.LOGTO['app_secret'],
    ),
    storage=SessionStorage(),
)