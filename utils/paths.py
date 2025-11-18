from datetime import datetime
from pathlib import Path

root_dir = Path(__file__).parent.parent
allure_results_dir = root_dir / "allure-results"
allure_report_dir = root_dir / "allure-report"
logging_config_yaml_path = root_dir / "logging_config.yaml"
