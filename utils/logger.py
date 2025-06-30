import logging
import os
from datetime import datetime

log = logging.getLogger("eCommLogger")
log.setLevel(logging.DEBUG)

LOG_FORMAT = "%(asctime)s — %(levelname)s — %(message)s"


def setup_file_logger(scenario_name: str, logs_dir: str):
    """Set up logger for each scenario with a unique log file."""
    global log
    log.handlers.clear()

    os.makedirs(logs_dir, exist_ok=True)

    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    file_name = f"{'_'.join(scenario_name.split()).strip()}_{timestamp}_logs.log"
    log_file_path = os.path.join(logs_dir, file_name)

    # File handler
    file_handler = logging.FileHandler(log_file_path, mode='a', encoding='utf-8')
    file_handler.setFormatter(logging.Formatter(LOG_FORMAT))
    log.addHandler(file_handler)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(logging.Formatter(LOG_FORMAT))
    log.addHandler(console_handler)

    return log_file_path
