#!/usr/bin/env python

import max7219.led as led
import time
import onetimepass as otp
import json
from datetime import datetime

def date(device, deviceId):

    now = datetime.now()
    day = now.day
    month = now.month
    year = now.year - 2000

    # Set day
    device.letter(deviceId, 8, int(day / 10))     # Tens
    device.letter(deviceId, 7, day % 10)          # Ones
    device.letter(deviceId, 6, '-')               # dash
    # Set day
    device.letter(deviceId, 5, int(month / 10))     # Tens
    device.letter(deviceId, 5, int(month / 10))     # Tens
    device.letter(deviceId, 4, month % 10)     # Ones
    device.letter(deviceId, 3, '-')               # dash
    # Set day
    device.letter(deviceId, 2, int(year / 10))     # Tens
    device.letter(deviceId, 1, year % 10)     # Ones


def clock(device, deviceId):

    now = datetime.now()

    utc = datetime.utcnow()
    hour = now.hour
    utc_hour = utc.hour
    minute = now.minute
    utc_minute = utc.minute
    second = now.second
    dot = second % 2 == 0   # calculate blinking dot

    # Set hours
    device.letter(deviceId, 8, int(hour / 10))     # Tens
    device.letter(deviceId, 4, int(utc_hour / 10))

    device.letter(deviceId, 7, hour % 10, dot)     # Ones
    device.letter(deviceId, 3, utc_hour % 10, dot)
    # Set minutes
    device.letter(deviceId, 6, int(minute / 10))   # Tens
    device.letter(deviceId, 2, int(utc_minute / 10))
    device.letter(deviceId, 5, minute % 10)        # Ones
    device.letter(deviceId, 1, utc_minute % 10)


def pixel(device, x, y, value, redraw=True):

    if value:
        device._buffer[x] |= (1 << y)
    else:
        device._buffer[x] &= ~(1 << y)

    if redraw:
        device.flush()


def set_led(device, row, col, state):
    if (state):
        pixel(device, col, row, 1)
    else:
        pixel(device, col, row, 0)


def draw_wide_row(device, n, r):

    set_led(device, r, 0, ((n & 8) >> 3))
    set_led(device, r, 1, ((n & 8) >> 3))

    set_led(device, r, 2, ((n & 4) >> 2))
    set_led(device, r, 3, ((n & 4) >> 2))

    set_led(device, r, 4, ((n & 2) >> 1))
    set_led(device, r, 5, ((n & 2) >> 1))

    set_led(device, r, 6, (n & 1))
    set_led(device, r, 7, (n & 1))


def draw_bcd_row(device, n, r):
    tens = n // 10
    ones = n % 10

    set_led(device, r, 0, ((tens & 8) >> 3))
    set_led(device, r, 1, ((tens & 4) >> 2))

    set_led(device, r, 2, ((tens & 2) >> 1))
    set_led(device, r, 3, (tens & 1))

    set_led(device, r, 4, ((ones & 8) >> 3))
    set_led(device, r, 5, ((ones & 4) >> 2))

    set_led(device, r, 6, ((ones & 2) >> 1))
    set_led(device, r, 7, (ones & 1))

def binary_clock(device):
    dt = datetime.now()
    hour = dt.hour
    if (dt.hour > 12):
        hour = dt.hour - 12

    draw_wide_row(device, hour, 0)
    draw_wide_row(device, hour, 1)

    draw_bcd_row(device, dt.minute, 3)
    draw_bcd_row(device, dt.second, 5)

def totp(device, deviceId, secret):
    token = otp.get_totp(secret)
    device.write_number(deviceId, value=token)

# Main Program
device = led.sevensegment(cascaded=3)
device.brightness(0)

with open('config.json') as json_data_file:
    config = json.load(json_data_file)

secret = config['otp']['secret']

while True:
    time.sleep(.5)
    totp(device, 2, secret)
    binary_clock(device)
    clock(device, 1)
