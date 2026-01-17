import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(BASE_DIR, "logs")
LOG_FILE = os.path.join(LOG_DIR, "security.log")

def log_event(ip, payload, result):
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

    with open(LOG_FILE, "a") as log:
        log.write(f"{datetime.now()} | IP: {ip} | {result} | {payload}\n")
