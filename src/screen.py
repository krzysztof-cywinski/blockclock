from PIL import Image, ImageDraw, ImageFont
from TP_lib import EPD_WIDTH, EPD_HEIGHT

from util import get_pic_dir, get_font_dir

class Screen():
  def __init__(self, name: str):
    self.name = name
    self.image = Image.new('1', (EPD_WIDTH, EPD_HEIGHT), 255)
    self.draw = DrawImage = ImageDraw.Draw(self.image)

  def handle_touch_input(self, x: int, y: int):
    pass

  def render(self) -> Image:
    pass

class MenuScreen(Screen):
  def __init__(self):
    super.__init__("Menu")

  def render(self) -> Image:
    return Image.open(os.path.join(picdir, 'Menu.bmp'))

class TextScreen(Screen):
  def __init__(self, font: str, font_size: int, initial_text: str = ''):
    super.__init__("Text")
    self.text = initial_text
    self.font = ImageFont.truetype(os.path.join(get_font_dir(), font), font_size)
    self.font_size = font_size

  def render(self) -> Image:
    self.draw.text((2, 2), u'testing ₿', font=self.font, fill=0)
    return self.image