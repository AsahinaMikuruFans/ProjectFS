import math

from source.core.math.Matrix import mat3
from source.core.math.Vector import vec2


class Transform:
    def __init__(self):
        # self.__currentMat = mat3()
        self.__matStack = [mat3()]

    def getMatStack(self):
        return self.__matStack.copy()

    def getCurrentMat(self):
        return self.__matStack[0].copy()
        # return self.__currentMat.copy()

    def push(self):
        mat = self.__matStack[0]
        self.__matStack.insert(0, mat)

    def pop(self):
        if len(self.__matStack) > 1:
            self.__matStack.pop(0)
            # self.__currentMat = self.__matStack[0]

    def popAll(self):
        # self.__currentMat = mat3()
        self.__matStack.clear()
        self.__matStack.append(mat3())

    def resetCurrentMat(self):
        self.__matStack[0] = mat3()
        # self.__currentMat = mat3()

    def resetAll(self):
        # self.__currentMat = mat3()
        for i in range(len(self.__matStack)):
            self.__matStack[i] = mat3()

    def scale(self):
        pass

    def translate(self, *args):
        tx, ty = 0, 0
        if len(args) == 1:
            v = args[0]
            if isinstance(v, list) or isinstance(v, tuple):
                tx, ty = v[0], v[1]
            if isinstance(v, vec2):
                tx, ty = v.x, v.y
        else:
            tx, ty = args[0], args[1]
        _m = mat3()
        _m.set(0, 2, tx)
        _m.set(1, 2, ty)
        # self.__currentMat = _m * self.__currentMat
        self.__matStack[0] = self.__matStack[0] * _m

        # self.__matStack[0] = self.__currentMat

    def rotate(self, *args):
        x, y, angle = 0, 0, 0
        if len(args) == 3:
            x, y, angle = args[0], args[1], args[2]
        elif len(args) == 1:
            angle = args[0]
        elif len(args) == 2:
            v = args[0]
            angle = args[1]
            if isinstance(v, vec2):
                x, y = v.x, v.y
            elif isinstance(v, list) or isinstance(v, tuple):
                x, y = v[0], v[1]

        sin_a, cos_a = math.sin(angle), math.cos(angle)
        _m = mat3()
        _m[0] = cos_a, -sin_a, 0
        _m[1] = sin_a, cos_a, 0
        _mL = mat3()
        _mL[0] = 1, 0, x
        _mL[1] = 0, 1, y
        _mR = mat3()
        _mR[0] = 1, 0, -x
        _mR[1] = 0, 1, -y

        _m = _mL * _m
        _m = _m * _mR

        # self.__currentMat = _m * self.__currentMat
        self.__matStack[0] = self.__matStack[0] * _m

        # self.__matStack[0] = self.__currentMat


# m = Transform()
# m.translate(10, 0)
# print(m.getMatStack())
# m.push()
# m.translate(70, 0)
# print(m.getMatStack())
