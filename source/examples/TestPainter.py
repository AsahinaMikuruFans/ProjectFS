import math
import random

from source.core.math.MathConst import PI
from source.core.math.Shape import Line, Rectangle, Triangle, Circle, Ellipse, Ray
from source.core.math.Vector import vec2, point2
from source.core.assembly.Painter import Painter
from source.view.baseClazz.Scene import Scene


class TestPainterScene(Scene):
    def __init__(self, screen, config, startClock):
        super(TestPainterScene, self).__init__(screen, config, startClock)
        self.painter = Painter(self.screen)
        self.points = []
        for i in range(0, 6):
            x = random.randint(0, 800)
            y = random.randint(0, 400)
            self.points.append(vec2(x, y))
        self.rect = Rectangle(400, 100, 200, 100)
        self.line = Ray(vec2(200, 200), math.radians(30), 400)
        self.white = (255, 255, 255)
        self.tra = Triangle(point2(100, 100), point2(60, 180), point2(140, 180))
        self.circle = Circle(400, 300, 100)
        self.ellipse = Ellipse(400, 300, 160, 70)

    def draw(self):
        # self.painter.Pixel(point2(700, 500), self.white)
        # self.painter.Triangle(self.tra, self.white, 0, 1)
        # self.painter.Rect(self.rect, self.white, 0, 1)
        # self.painter.Circle(self.circle, (255, 255, 255), 1)
        # self.painter.Ellipse(self.ellipse, self.white, 1)
        self.painter.Lines(self.points, (255, 255, 255), 1, 1, 1)
        # self.painter.Line(self.line, (255, 255, 255), 1, 0)
        # self.painter.Lines((point2(200, 200), point2(400, 400)), (255, 255, 255), 1, 0, 1)
        self.painter.push()
        self.painter.scale(self.points[0].x, self.points[0].y, 0.5, 0.5)
        self.painter.Lines(self.points, (255, 0, 0), 1, 1, 1)
        # self.painter.Lines((point2(200, 200), point2(400, 400)), (255, 0, 0), 1, 0, 1)
        self.painter.pop()
        # self.painter.Line(self.line, (255, 0, 0), 1, 0)
