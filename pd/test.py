#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from SimpleCV import Color, Image
img = Image("images/dark.png")

try:
    blue_distance = img.hueDistance(Color.BLUE).invert()
    blobs = blue_distance.findBlobs()
    blobs.draw(color=Color.PUCE, width=3)
    img.addDrawingLayer(blue_distance.dl())
    img.show()
    time.sleep(10)
except:
    print('kill')
