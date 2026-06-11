from us_visa.exception import USvisaException
from us_visa.logger import logging
import sys


try:
    r=3/0
    print(r)
except Exception as e:
    raise USvisaException(e , sys)
    