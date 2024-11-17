import os

from PIL import Image, ImageDraw, ImageFont
from TP_lib import epd2in13_V4

from util import get_pic_dir, get_font_dir


class Screen():
  def __init__(self, name: str, epd: epd2in13_V4.EPD):
    self.name = name
    self.width = epd.height # this is transposed later
    self.height = epd.width # this is transposed later
    self.image = Image.new('1', (epd.height, epd.width), 255)
    self.draw = DrawImage = ImageDraw.Draw(self.image)
    self.isDirty = True

  def handle_touch_input(self, x: int, y: int):
    pass

  def render(self) -> Image:
    self.child_render()
    self.isDirty = False
    return self.image.transpose(Image.ROTATE_270)

  def child_render(self):
    # change the internal image
    pass


class MenuScreen(Screen):
  def __init__(self, epd: epd2in13_V4.EPD):
    super(MenuScreen, self).__init__("Menu", epd)

  def render(self) -> Image:
    return Image.open(os.path.join(picdir, 'Menu.bmp'))


class TextScreen(Screen):
  def __init__(self, epd: epd2in13_V4.EPD, font: str, font_size: int, initial_text: str = ''):
    super(TextScreen, self).__init__("Text", epd)
    self.text = initial_text
    self.font = ImageFont.truetype(
        os.path.join(get_font_dir(), font), font_size)
    self.font_size = font_size

  def set_text(self, text:str):
    self.text = text
    self.isDirty = True;

  def child_render(self) -> Image:
    self.draw.text((self.width/2, self.height/2), self.text, font=self.font, fill=0, anchor='mm')
    self.isDirty = False
    return self.image
