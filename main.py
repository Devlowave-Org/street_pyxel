import pyxel
import math
import numpy
import time
import random

class App:
    def __init__(self):
        pyxel.init(128, 128, "Street_Pyxel", 60, pyxel.KEY_ESCAPE)


class Fighter:
    def __init__(self):
        pass

    def update(self):
        if pyxel.btnp(pyxel.KEY_D):
            self.move('right')
        if pyxel.btnp(pyxel.KEY_Q):
            self.move('left')
        if pyxel.btnp(pyxel.KEY_Z):
            self.move('up')

    def draw(self):
        pass

    def move(self, direction):
        pass
App()