from os import path

from rinoh.font import Typeface
from rinoh.font.style import REGULAR, BOLD, ITALIC
from rinoh.font.opentype import OpenTypeFont


__all__ = ['typeface']


def otf(style):
    filename = 'DejaVuSerif{}.ttf'.format(style)
    return path.join(path.dirname(__file__), filename)


typeface = Typeface('DejaVuSerif',
                    OpenTypeFont(otf(''), weight=REGULAR),
                    OpenTypeFont(otf('-Italic'), weight=REGULAR, slant=ITALIC),
                    OpenTypeFont(otf('-Bold'), weight=BOLD),
                    OpenTypeFont(otf('-BoldItalic'), weight=BOLD, slant=ITALIC))
