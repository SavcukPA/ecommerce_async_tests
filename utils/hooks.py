import hashlib
import shutil
import subprocess
import logging
from datetime import datetime
from pathlib import Path

logger = logging.getLogger(__name__)


def copy_last_history(allure_report_dir: Path, allure_results_dir: Path):
    """
    Копирует историю из последнего отчета в allure-results для трендов.
    """
    if not allure_report_dir.exists():
        return

    reports = sorted(
        [d for d in allure_report_dir.iterdir() if d.is_dir()], reverse=True
    )
    for report in reports:
        history_dir = report / "history"
        if history_dir.exists():
            dest = allure_results_dir / "history"
            dest.mkdir(parents=True, exist_ok=True)
            for file in history_dir.iterdir():
                shutil.copy(file, dest)
            logger.info(f"История скопирована из {history_dir} в {dest}")
            break


def generate_allure_report(path_allure_results_dir: Path, path_allure_report_dir: Path):
    """
    Генерация отчетов allure
    :param path_allure_results_dir: путь к директории с allure-results
    :param path_allure_report_dir: путь к директории для сохранения отчетов
    :return:
    """
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    path_allure_report_dir = path_allure_report_dir / timestamp
    path_allure_report_dir.mkdir(parents=True, exist_ok=True)

    logger.info("Генерация отчета Allure")
    logger.info(f"Allure results: {path_allure_results_dir}")
    logger.info(f"Allure report: {path_allure_report_dir}")

    command = f'allure generate "{path_allure_results_dir}" -o "{path_allure_report_dir}" --clean'
    logger.info(f"Выполняем команду: {command}")

    try:
        subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        logger.info(f"✅ Allure отчет успешно сгенерирован: {path_allure_report_dir}")
        return path_allure_report_dir
    except subprocess.CalledProcessError as e:
        logger.error(f"❌ Ошибка при генерации Allure отчета:\n{e.stderr}")
        return None
