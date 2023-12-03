import logging
import os
import sys
from datetime import datetime
import logging.handlers

from rest.RestInitializer import init_flask

def init_logger():
    
    log_dir = "logs"
    execution_date = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    log_file_name = log_dir + "/" + execution_date + ".log"
    
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    else:
        logs_list = sorted(os.listdir(log_dir))
        if len(logs_list) > 2:
            os.remove(log_dir + "/" + logs_list[0])

    debug_handles = [
        logging.FileHandler(log_file_name),
        logging.FileHandler(log_dir + "/latest.log", mode="w"),
        logging.StreamHandler(sys.stdout)
    ]
    
    logging.basicConfig (
        format="[%(asctime)s] %(module)s:%(lineno)d %(levelname)s\t%(message)s",
        handlers=debug_handles,
        level=logging.INFO
    )


if __name__ == "__main__":
    init_logger()
    init_flask()