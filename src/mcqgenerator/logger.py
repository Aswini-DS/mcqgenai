import logging
import os
import traceback
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

current_path = os.getcwd()
log_path = os.path.join(current_path,'logs')
os.makedirs(log_path,exist_ok=True)

LOG_FILEPATH = os.path.join(log_path,LOG_FILE)


logging.basicConfig(level=logging.INFO,
        filename=LOG_FILE,
        format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
)