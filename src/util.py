import os

def get_img_dir() -> str:
  return os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'img')

def get_font_dir() -> str:
  return os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'font')

def get_lib_dir() -> str:
  return os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
