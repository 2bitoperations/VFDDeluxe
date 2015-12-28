import logging
import serial
import datetime
import time
import sys

rootLogger = logging.getLogger()
rootLogger.setLevel(logging.DEBUG)

ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
rootLogger.addHandler(ch)

fileLogger = logging.FileHandler("./server.log")
fileLogger.setLevel(logging.INFO)
fileLogger.setFormatter(formatter)
rootLogger.addHandler(fileLogger)

ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)

# display stupid animation just because
def draw_single(data, sleep):
    for c in list(data):
        ser.write("!9%s%s%s%s%s%s" % (c, c, c, c, c, c))
        time.sleep(sleep)

def draw_time(now):
    time_as_string = now.strftime("%H%M%S")
    logging.debug("time is %s" % time_as_string)
    ser.write("!9%s" % time_as_string)

def sleep_till_next_sec():
    sleep_now = datetime.datetime.now()
    micros_to_sleep = 1000000 - sleep_now.microsecond
    secs_to_sleep = micros_to_sleep / 1000000.0
    logging.debug("sleeping %s micros, %s sec" % (micros_to_sleep, secs_to_sleep))
    time.sleep(secs_to_sleep)

draw_single("1234567890_<`^'>_-8 ", .2)
while True:
    now = datetime.datetime.now()
    if now.minute == 0:
        draw_single("_<`^'>_-8 ", .2)
        now = datetime.datetime.now()

    draw_time(now)
    sleep_till_next_sec()

