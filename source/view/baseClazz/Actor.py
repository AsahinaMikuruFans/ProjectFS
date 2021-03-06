import pygame

from source.core.math.Shape import Rectangle


class Actor:
    def __init__(self, texture, area=None, physicalBody=None, visual=True, zIndex=0, active=False):
        self.texture = texture
        self.visual = visual
        self.zIndex = zIndex
        self.physicalBody = physicalBody
        self.active = active
        self.area = area
        if self.area is None:
            w = self.texture.get_rect().w
            h = self.texture.get_rect().h
            self.area = Rectangle(0, 0, w, h)
        else:
            self.texture = pygame.transform.scale(self.texture, (self.area.w, self.area.h))
        self.initArea = self.area

    def collided(self, othActor):
        if not isinstance(othActor, Actor):
            raise Exception("Class '{}' must is a subclass of 'Actor'".format(othActor))
        return self.area.intersects(othActor.area)

    def update(self, *args):
        pass

    def draw(self, screen):
        screen.blit(self.texture, self.area.local())


# class ActorGroup:
#     def __init__(self, activeArea, *args):
#         self.actors = []
#         for p in args:
#             if not isinstance(p, Actor):
#                 raise Exception("Class '{}' must is a subclass of 'Actor'".format(p))
#             self.actors.append(p)
#         if not isinstance(activeArea, Shape):
#             raise Exception("Class '{}' must is a subclass of 'Shape'".format(activeArea))
#         self.activeArea = activeArea
#         self.__activeArea = RectangleRange(activeArea.w / 2, activeArea.h / 2, activeArea.w / 2, activeArea.h / 2)
#         self.__quadTree = QuadTree(self.__activeArea, 4)
#         self.__collideDict = {}
#
#     def add(self, *actors):
#         for a in actors:
#             if not isinstance(a, Actor):
#                 raise Exception("Class '{}' must is a subclass of 'Actor'".format(a))
#             self.actors.append(a)
#
#     def remove(self, actor):
#         if actor in self.actors:
#             self.actors.remove(actor)
#
#     def size(self):
#         return len(self.actors)
#
#     def update(self):
#         self.__quadTree = QuadTree(self.__activeArea, 4)
#         self.__collideDict.clear()
#
#         for a in self.actors:
#             if not a.frozen:
#                 a.update()
#                 node = Node(a.collideArea.x, a.collideArea.y, a)
#                 self.__quadTree.insert(node)
#
#     def draw(self, screen):
#         for a in self.actors:
#             if a.visual:
#                 a.draw(screen)
#
#     def getCollideDict(self):
#         for e in self.actors:
#             _list = []
#             _range = RectangleRange(e.collideArea.x, e.collideArea.y, e.collideArea.w * 2, e.collideArea.h * 2)
#             sprites = self.__quadTree.query(_range)
#             for _s in sprites:
#                 if e is not _s.data and e.collided(_s.data):
#                     _list.append(_s.data)
#             if _list:
#                 self.__collideDict[e] = _list
#         return self.__collideDict
#
#     def getCollideList(self, actor, isDel):
#         _lis = []
#         if not isinstance(actor, ActorGroup):
#             raise Exception("Class '{}' must is a subclass of 'Actor'".format(actor))
#         for a in self.actors:
#             if a.collided(actor):
#                 _lis.append(a)
#                 if isDel:
#                     self.remove(a)
#         return _lis
#
#     def getCollide_with_Oth(self, oth):
#         raise Exception("function 'getCollide_with_Oth' not implemented")
#         # if not isinstance(oth, ActorGroup):
#         #     raise Exception("Class '{}' must is a subclass of 'ActorGroup'".format(oth))
#         # if not self.activeArea.same(oth.activeArea):
#         #     temp_new_area = Rectangle()
#         # temp_group = ActorGroup(oth.activeArea, oth.actors)
#         # temp_group.add(self.actors)



