from src.logger import logging
from src.exception import CustomException
import sys

logging.info("Application Started")

try:
    logging.info("Trying to divide numbers")

    a = 10
    b = 0

    result = a / b

    logging.info(f"Result = {result}")

except Exception as e:
    logging.error("Division failed")
    raise CustomException(e, sys)