from pathlib import Path

root_path = Path.cwd().resolve().parent

download_dir = root_path / "data" / "downloads"
download_dir.mkdir(parents=True, exist_ok=True)
