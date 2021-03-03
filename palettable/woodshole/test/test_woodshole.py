from __future__ import absolute_import

from ... import woodshole as whp


def test_print_maps(capsys):
    whp.print_maps()
    out, err = capsys.readouterr()
    lines = out.split('\n')
    assert lines[0] == 'whoi       qualitative     6'


def test_get_map():
    palette = whp.get_map('wHoI')
    assert isinstance(palette, whp.woodshole.WoodsHoleMap)
    assert palette.name == 'whoi'
    assert palette.type == 'qualitative'
    assert len(palette.colors) == 6
    assert palette.url == \
        ('https://github.com/shu251/PaletteWoodsHole/blob/master/images/whoi-logo.png')


def test_get_map_reversed():
    palette = wap.get_map('wHoI', reverse=True)
    assert isinstance(palette, whp.woodshole.WoodsHoleMap)
    assert palette.name == 'whoi_r'
    assert palette.type == 'qualitative'
    assert len(palette.colors) == 6
    assert palette.url == \
        ('https://github.com/shu251/PaletteWoodsHole/blob/master/images/whoi-logo.png')


def test_palettes_loaded():
    assert isinstance(whp.whoi_6, whp.woodshole.WoodsHoleMap)
    assert isinstance(whp.whoi_6_r, whp.woodshole.WoodsHoleMap)
    assert whp.whoi_6.type == 'qualitative'


def test_get_all_maps():
    # Smoke tests.
    whp._get_all_maps()
