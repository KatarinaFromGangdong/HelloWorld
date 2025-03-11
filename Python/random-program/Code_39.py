# !/usr/bin/env python
# -*- coding: utf-8 -*-

import barcode
from barcode.writer import ImageWriter

EAN = barcode.get_barcode_class('code39')
ean = EAN(u'password', writer=ImageWriter())
fullname = ean.save('my_code39_barcode')
