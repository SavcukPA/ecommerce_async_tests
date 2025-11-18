import logging
import logging.config
import yaml
import os
from pathlib import Path

from config import settings


def setup_logging(
    default_path="logging_config.yaml",
):
    """Настройка логирования из YAML файла."""
    logging_level = settings.logger.log_level
    if os.path.exists(default_path):
        with open(default_path, "rt") as f:
            config = yaml.safe_load(f)

        # Создаем директорию для логов если её нет
        log_dir = Path("logs")
        log_dir.mkdir(exist_ok=True)

        # Применяем конфигурацию
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=logging_level)
