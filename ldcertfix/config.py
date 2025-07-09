"""Helper module for persisting user configuration."""

import json
from pathlib import Path

CONFIG_PATH = Path('ldcertfix_config.json')


def load_config() -> dict:
    """Return the configuration dictionary or an empty one if unavailable."""
    if CONFIG_PATH.exists():
        try:
            with CONFIG_PATH.open('r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            return {}
    return {}


def save_config(data: dict) -> None:
    """Persist ``data`` to ``CONFIG_PATH`` if possible."""
    try:
        with CONFIG_PATH.open('w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception:
        pass
