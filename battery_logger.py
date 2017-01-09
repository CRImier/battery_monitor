#!/usr/bin/env python
from max1704x import MAX1704x
from time import sleep
from datetime import datetime
import logging

logging.basicConfig(filename="/root/battery.log", level=logging.INFO)

fuel_gauge = MAX1704x()
print("Initial value: {}".format(fuel_gauge.get_soc()))

while True:
    soc = fuel_gauge.get_soc()
    now = datetime.now()
    logging.info("{} at {:%H:%M:%S, %B %d, %Y}".format(soc, now))
    sleep(60)
