from __future__ import absolute_import
from __future__ import print_function
"""
Color palettes gratefully copied from https://github.com/shu251/PaletteWoodsHole.

"""

import webbrowser

from ..palette import Palette

def hex2rgb(hex_list): 
    rgb = [] 
    for h in hex_list: 
        a = h.lstrip('#')
        hlen = len(a)
        rgb.append(tuple(int(a[i:i+hlen//3], 16) for i in range(0,hlen,hlen//3))) 
    return rgb 


_tumblr_template = 'https://github.com/shu251/PaletteWoodsHole/blob/master/images/{0}'
_palette_type = 'qualitative'

# Tumblr palettes in chronological order
_palettes = {
    'whoi': {
        'colors': [
            (4, 30, 66), (0, 169, 224), (0, 105, 177), (0, 183, 189), (83, 86, 90), (187, 188, 188)
        ],
        'type': _palette_type,
        'url': _tumblr_template.format('whoi-logo.png')
    },
    'whoisec': {
        'colors': [
            (255, 209, 0), (238, 83, 64), (230, 231, 232), (183, 191, 16)
        ],
        'type': _palette_type,
        'url': _tumblr_template.format('whoi-logo.png')
    },
    'alvin': {
        'colors': [(219, 252, 253), (239, 106, 63), (20, 81, 120), (219, 219, 219), (35, 49, 51), (37, 124, 155), (255, 255, 255)
        ],
        'type': _palette_type,
        'url': _tumblr_template.format('alvin.png')
    },
    'jason': {
        'colors': [(4, 79, 154), (254, 196, 79), (93, 134, 195), (252, 78, 42), (182, 200, 219), (42, 57, 79)
        ],
        'type': _palette_type,
        'url': _tumblr_template.format('jason.jpg')
    },
    'atlantis': {
        'colors': [(157, 186, 187), (27, 51, 75), (207, 188, 159), (87, 111, 112), (9, 26, 42), (48, 22, 9), (224, 229, 229), (89, 104, 115), (135, 138, 126)
        ],
        'type': _palette_type,
        'url': _tumblr_template.format('Atlantis.jpg')
    },
    'wefa_sun': {
        'colors': [(221, 199, 148), (181, 98, 58), (249, 83, 22), (88, 68, 56), (238, 186, 98), (140, 59, 37), (155, 142, 119), (145, 112, 98)
        ],
        'type': _palette_type,
        'url': _tumblr_template.format('west-fal-sunset.jpg')
    },
    'bikepath': {
        'colors': [(108, 104, 101), (89, 94, 68), (134, 144, 85), (225, 223, 234), (49, 62, 28), (208, 212, 220), (188, 178, 119)
        ],
        'type': _palette_type,
        'url': _tumblr_template.format('shiningsea.jpg')
    },
    'bog': {
        'colors': [(172, 112, 112), (214, 217, 218), (51, 41, 27), (197, 199, 199), (147, 119, 113), (90, 74, 53)
        ],
        'type': _palette_type,
        'url': _tumblr_template.format('cranberrybog.jpg')
    },
    'rocky_beach': {
        'colors': [(113, 99, 71), (71, 106, 167), (114, 153, 206), (162, 147, 122), (178, 201, 227), (61, 48, 25)
        ],
        'type': _palette_type,
        'url': _tumblr_template.format('rocky-beach.jpg')
    },
    'eelpond_winter': {
        'colors': [(225, 231, 237), (197, 201, 207), (53, 54, 56), (106, 112, 114), (170, 174, 179), (255, 255, 255)
        ],
        'type': _palette_type,
        'url': _tumblr_template.format('eel-pond-winter.jpg')
    },
    'tulips': {
        'colors': [(215, 125, 54), (228, 191, 98), (121, 128, 94), (226, 219, 199), (129, 160, 99),
 (250, 159, 181), (178, 66, 54), (254, 217, 118), (90, 115, 86)
        ],
        'type': _palette_type,
        'url': _tumblr_template.format('spring.jpg')
    },
    'sunset_winter': {
        'colors': [(253, 234, 171), (233, 178, 122), (168, 177, 189), (181, 137, 117), (219, 219, 210), (246, 231, 193)
        ],
        'type': _palette_type,
        'url': _tumblr_template.format('sunset-winter.jpg')
    },
    'dock': {
        'colors': [(111, 169, 228), (164, 114, 63), (87, 115, 131), (248, 245, 229), (209, 171, 138), (251, 219, 154), (92, 94, 94), (161, 37, 49), (89, 55, 43)
        ],
        'type': _palette_type,
        'url': _tumblr_template.format('dock.png')
    },
    'marsh': {
        'colors': [(91, 42, 20), (174, 93, 63), (160, 46, 53), (102, 84, 56), (162, 127, 65), (169, 145, 82), (215, 197, 152), (118, 125, 39), (140, 137, 135)
        ],
        'type': _palette_type,
        'url': _tumblr_template.format('marsh.png')
    },
    'knob': {
        'colors': [(109, 99, 95), (69, 84, 85), (146, 153, 153), (216, 199, 174), (244, 192, 136), (255, 250, 120), (245, 143, 82), (235, 101, 37)
        ],
        'type': _palette_type,
        'url': _tumblr_template.format('knob1.png')
    },
    'naushon': {
        'colors': [(150, 161, 185), (230, 203, 169), (133, 104, 65), (221, 149, 113), (91, 91, 138), (198, 123, 51)
        ],
        'type': _palette_type,
        'url': _tumblr_template.format('naushon.png')
    },
    'long_pond': {
        'colors': [(201, 164, 86), (226, 119, 65), (203, 78, 7), (138, 155, 94), (100, 56, 48), (171, 201, 203), (218, 181, 118), (176, 64, 41)
        ],
        'type': _palette_type,
        'url': _tumblr_template.format('longpond.png')
    },
    'siders': {
        'colors': [(184, 191, 208), (248, 235, 218), (253, 231, 196), (249, 199, 159), (109, 63, 35), (120, 118, 119), (75, 66, 124), (26, 79, 40)
        ],
        'type': _palette_type,
        'url': _tumblr_template.format('siders.png')
    },
    'siders_filters': {
        'colors': [(216, 198, 142), (178, 154, 67), (170, 142, 113), (104, 75, 50), (142, 113, 84)
        ],
        'type': _palette_type,
        'url': _tumblr_template.format('siders.png')
    },
    'siders_summer': {
        'colors': [(115, 142, 192), (67, 86, 51), (85, 112, 161), (100, 120, 37), (243, 101, 86), (156, 160, 214)
        ],
        'type': _palette_type,
        'url': _tumblr_template.format('siders-summer.png')
    },
}

_map_names = {}
for k in _palettes:
    _map_names[k.lower()] = k


class WoodsHoleMap(Palette):
    """
    Representation of a color map with matplotlib compatible
    views of the map.

    Parameters
    ----------
    name : str
    map_type : str
    colors : list
        Colors as list of 0-255 RGB triplets.
    url : str
        URL on the web where this color map can be viewed.

    Attributes
    ----------
    name : str
    type : str
    number : int
        Number of colors in color map.
    colors : list
        Colors as list of 0-255 RGB triplets.
    hex_colors : list
    mpl_colors : list
    mpl_colormap : matplotlib LinearSegmentedColormap
    whp_url : str
        URL on the web where this color map can be viewed.

    """
    def __init__(self, name, map_type, colors, url):
        super(WoodsHoleMap, self).__init__(name, map_type, colors)
        self.url = url

    def whp(self):
        """
        View this color palette on the web.
        Will open a new tab in your web browser.

        """
        webbrowser.open_new_tab(self.url)  # pragma: no cover


def print_maps():
    """
    Print a list of Woods Hole palettes.

    """
    namelen = max(len(k) for k in _palettes)
    fmt = '{0:' + str(namelen + 4) + '}{1:16}{2:}'

    for k in sorted(_palettes.keys()):
        print(fmt.format(k, _palettes[k]['type'], len(_palettes[k]['colors'])))


def get_map(name, reverse=False):
    """
    Get a Woods Hole palette by name.

    Parameters
    ----------
    name : str
        Name of map. Use palettable.woodshole.print_maps
        to see available names.
    reverse : bool, optional
        If True reverse colors from their default order.

    Returns
    -------
    palette : WoodsHoleMap

    """
    name = _map_names[name.lower()]
    palette = _palettes[name]

    if reverse:
        name += '_r'
        palette['colors'] = list(reversed(palette['colors']))

    return WoodsHoleMap(
        name, palette['type'], palette['colors'], palette['url'])


def _get_all_maps():
    """
    Returns a dictionary of all Woods Hole palettes,
    including reversed ones.

    """
    fmt = '{0}_{1}'.format
    d = dict(
        (fmt(name, m.number), m)
        for name, m in ((name, get_map(name)) for name in _palettes))
    fmt = '{0}_{1}_r'.format
    d.update(
        dict(
            (fmt(name, m.number), m)
            for name, m in (
                (name, get_map(name, reverse=True)) for name in _palettes)))
    return d
