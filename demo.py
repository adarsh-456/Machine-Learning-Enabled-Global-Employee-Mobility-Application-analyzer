import sys
from visa.logger import logging
from visa.exception import USvisaException

try:
    a = 1 / 0
except Exception as e:
    raise USvisaException(e, sys)