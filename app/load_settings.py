# settings_reader.py
import tomllib
from typing import Any

settings: dict[str, Any] = {}

try:
    with open(file="app/settings.toml", mode="rb") as f:
        settings = tomllib.load(f)
except FileNotFoundError as fne:
    raise fne
except Exception as e:
    raise e


# 설정값 읽기
def read_settings(key: str, section: str, sub_section: str) -> Any:

    value: Any

    value = settings[section][sub_section][key]

    return value
