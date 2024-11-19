import os

from PIL import Image, ImageDraw, ImageFont
from TP_lib import epd2in13_V4

from util import get_pic_dir, get_font_dir


class Screen():
  def __init__(self, name: str, epd: epd2in13_V4.EPD):
    self.name = name
    self.width = epd.height # this is transposed later
    self.height = epd.width

  def handle_touch_input(self, x: int, y: int):
    pass

  def render(self) -> Image:
    image = self.child_render()
    return image.transpose(Image.ROTATE_90)

  def child_render(self):
    # change the internal image
    pass


class TextScreen(Screen):
  def __init__(self, epd: epd2in13_V4.EPD, font: str, font_size: int, initial_text: str = ''):
    super(TextScreen, self).__init__("Text", epd)
    self.text = initial_text
    self.font = ImageFont.truetype(
        os.path.join(get_font_dir(), font), font_size)
    self.font_size = font_size

  def set_text(self, text:str):
    self.text = text

  def child_render(self) -> Image:
    image = Image.new('1', (self.width, self.height), 255)
    draw = ImageDraw.Draw(image)
    draw.text((self.width/2, self.height/2), self.text, font=self.font, fill=0, anchor='mm')
    return image

class BitcoinPriceScreen(Screen):
  def __init__(self, epd: epd2in13_V4.EPD):
    super(BitcoinPriceScreen, self).__init__("BitcoinPrice", epd)
    self.bitcoin_logo_font = ImageFont.truetype(
        os.path.join(get_font_dir(), 'paplane-regular.ttf'), 48)
    self.price_font = ImageFont.truetype(
        os.path.join(get_font_dir(), 'carre-regular.ttf'), 42)
    self.price = 0

  def set_price(self, price: int):
    self.text = text

  def child_render(self) -> Image:
    image = Image.new('1', (self.width, self.height), 255)
    draw = ImageDraw.Draw(image)
    draw.text((5, self.height/2), u'₿', font=self.bitcoin_logo_font, fill=0, anchor='lm')
    draw.text((self.width - 5, self.height/2), str(self.price),
              font=self.price_font, fill=0, anchor='rm')
    return image
