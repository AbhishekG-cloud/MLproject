import logging
import os
from datetime import datetime

# Generate log file name and log directory path
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_dir = os.path.join(os.getcwd(), "logs")

# Create the logs directory if it doesn't exist
os.makedirs(logs_dir, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# Print the paths to debug
print(f"Log directory: {logs_dir}")
print(f"Log file path: {LOG_FILE_PATH}")

try:
    logging.basicConfig(
        filename=LOG_FILE_PATH,
        format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO,
    )

    if __name__ == "__main__":
        logging.info("logging started")
        print("Logging setup complete.")

except Exception as e:
    print(f"Error setting up logging: {e}")
