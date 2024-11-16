import os

def get_pic_dir() -> str:
  return os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic/2in13')

def get_font_dir() -> str:
  return os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')

def get_lib_dir() -> str:
  return os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
