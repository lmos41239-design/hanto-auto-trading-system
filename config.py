import os
from dataclasses import dataclass


@dataclass
class Settings:
    mode: str
    stock_code: str
    quantity: int
    ma_window: int


def _load_env_file(path: str = ".env") -> None:
    if not os.path.exists(path):
        return

    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip())


def load_settings() -> Settings:
    _load_env_file()

    return Settings(
        mode=os.getenv("MODE", "simulation"),
        stock_code=os.getenv("STOCK_CODE", "005930"),
        quantity=int(os.getenv("QUANTITY", "1")),
        ma_window=int(os.getenv("MA_WINDOW", "5")),
    )
