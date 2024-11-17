#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
import requests
import time

from util import get_lib_dir, get_pic_dir, get_font_dir

picdir = get_pic_dir()
fontdir = get_font_dir()
libdir = get_lib_dir()
if os.path.exists(libdir):
    sys.path.append(libdir)

from TP_lib import gt1151
from TP_lib import epd2in13_V4
import time
import logging
from PIL import Image,ImageDraw,ImageFont
import traceback
import threading

from screen import TextScreen

logging.basicConfig(level=logging.WARN)
flag_t = 1

def get_btc_price() -> int:
    resp = requests.get(
        url='https://api.coinbase.com/v2/exchange-rates', params={'currency': 'BTC'})
    data = resp.json()
    price = data['data']['rates']['USD']
    return int(float(price))

btc_price = get_btc_price()

def pthread_irq():
    print("irq pthread running")
    while flag_t == 1 :
        if(gt.digital_read(gt.INT) == 0) :
            GT_Dev.Touch = 1
        else :
            GT_Dev.Touch = 0
    print("irq thread:exit")

def pthread_btc_price():
    print("price pthread running")
    while flag_t == 1:
        global btc_price
        btc_price = get_btc_price()
        logging.info(btc_price)
        time.sleep(2)
    print("price thread:exit")

try:
    logging.info("epd2in13_V4 Touch Demo")

    epd = epd2in13_V4.EPD()
    gt = gt1151.GT1151()
    GT_Dev = gt1151.GT_Development()
    GT_Old = gt1151.GT_Development()

    logging.info("init and Clear")

    epd.init(epd.FULL_UPDATE)
    gt.GT_Init()
    epd.Clear(0xFF)

    irq_t = threading.Thread(target=pthread_irq)
    irq_t.daemon = True
    irq_t.start()

    btc_price_t = threading.Thread(target=pthread_btc_price)
    btc_price_t.daemon = True
    btc_price_t.start()

    screen = TextScreen(epd, 'paplane-regular.ttf', 42)

    initialized = False
    while(1):
        screen.set_text(u'₿/$ '+str(btc_price))
        image = screen.render()
        if initialized:
            epd.displayPartial_Wait(epd.getbuffer(image))
        else:
            epd.displayPartBaseImage(epd.getbuffer(image))
            initialized = True

        # Read the touch input
        gt.GT_Scan(GT_Dev, GT_Old)
        if((GT_Old.X[0] != GT_Dev.X[0] or GT_Old.Y[0] != GT_Dev.Y[0] or GT_Old.S[0] != GT_Dev.S[0]) and GT_Dev.TouchpointFlag):
            GT_Dev.TouchpointFlag = 0
            logging.debug('Touched X={} Y={}'.format(GT_Dev.X[0], GT_Dev.Y[0]))

        time.sleep(2)

except IOError as e:
    logging.info(e)

except KeyboardInterrupt:
    logging.info("ctrl + c:")
    flag_t = 0
    epd.sleep()
    time.sleep(2)
    irq_t.join()
    btc_price_t.join()
    epd.Dev_exit()
    exit()
