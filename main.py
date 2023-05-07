import pyxel
import math
import numpy
import time
import random


class App:
    def __init__(self):
        pyxel.init(128, 128, "Street_Pyxel", 30, pyxel.KEY_ESCAPE)
        pyxel.load("sample.pyxres")
        self.fighter_left = Fighter("left")
        self.fighter_right = Fighter("right")

        pyxel.run(self.update, self.draw)

    def draw(self):
        pyxel.cls(0)
        self.fighter_left.draw()
        self.fighter_right.draw()

    def update(self):
        if self.fighter_left.collision(self.fighter_right.x):
            if pyxel.btn(pyxel.KEY_D):
                self.fighter_left.x += 1
            if pyxel.btn(pyxel.KEY_Q):
                self.fighter_left.x -= 1
            if pyxel.btn(pyxel.KEY_Z):
                pass
        if pyxel.btn(pyxel.KEY_LEFT):
            self.fighter_right.x -= 1
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.fighter_right.x += 1


class Fighter:

    def __init__(self, pos):
        if pos == "left":
            self.x = 30
        elif pos == "right":
            self.x = 100
        else:
            print("only accept left or right")

        self.y = 100
    def draw(self):
        pyxel.blt(self.x, self.y, 0, 128, 16, 16, 16, 0)

    def collision(self, x):
        if self.x < x or self.x > x + 16:
            return False




App()