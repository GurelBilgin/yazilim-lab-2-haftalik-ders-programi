
from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class MySQLConfig:
    """MySQL bağlantı bilgileri."""

    host: str
    user: str
    password: str
    database: str

    @classmethod
    def from_env(cls) -> "MySQLConfig":
        """Bağlantı bilgilerini ortam değişkenlerinden okur."""
        return cls(
            host=os.getenv("DB_HOST", "localhost"),
            user=os.getenv("DB_USER", "root"),
            password=os.getenv("DB_PASSWORD", ""),
            database=os.getenv("DB_NAME", "app"),
        )


class MySQLRepository:
    """Opsiyonel MySQL bağlantı katmanı.

    Orijinal projedeki MySQL yaklaşımını korumak isteyen kullanıcılar için
    bırakılmıştır. Bağımlılık olarak `mysql-connector-python` opsiyoneldir.
    """

    def __init__(self, config: MySQLConfig | None = None):
        self.config = config or MySQLConfig.from_env()

    def _connect(self) -> Any:
        try:
            import mysql.connector
        except ImportError as exc:
            raise RuntimeError(
                "MySQL kullanmak için `pip install .[mysql]` komutuyla opsiyonel bağımlılığı kurun."
            ) from exc

        return mysql.connector.connect(
            host=self.config.host,
            user=self.config.user,
            password=self.config.password,
            database=self.config.database,
        )

    def fetch_all(self, query: str, params: tuple | None = None) -> list[tuple]:
        """Sorgu sonucu tüm satırları döndürür."""
        conn = self._connect()
        cursor = conn.cursor()
        try:
            cursor.execute(query, params or tuple())
            return list(cursor.fetchall())
        finally:
            cursor.close()
            conn.close()
