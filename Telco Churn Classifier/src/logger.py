import os
import logging
from datetime import datetime


PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Setup Loagin Folder/Files
LOG_FOLDER_FORMAT = datetime.now().strftime('%d-%m-%Y_%H')
LOG_FILE_FORMAT = datetime.now().strftime('%d-%m-%Y_%H-%M') + ".log"


# Create Logs. Directory
log_path = os.path.join(PROJECT_ROOT, 'Logs', LOG_FOLDER_FORMAT)
os.makedirs(log_path, exist_ok=True)

# Create Log File
LOG_FILE = os.path.join(log_path, LOG_FILE_FORMAT)

logger = logging.getLogger()
logger.setLevel(logging.INFO)


# Prevent Duplicate Handlers
if not logger.handlers:
    file_handler = logging.FileHandler(LOG_FILE)
    formatter = logging.Formatter(
        '[%(asctime)s] - %(name)s - %(levelname)s - '
        '[%(filename)s:%(lineno)d] - %(message)s'
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)