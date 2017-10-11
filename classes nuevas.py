#Encoding
# -*- coding: utf-8 -*-
area = 0
class Figura(object):

    def __int__(self,area):
        self.__area = 0

class Cuadro(Figura):

    def __init__(self, area, base, altura):
        self.base = base
        self.altura = altura
        self.area = area


    def calcular_area(self):

        self.area = self.base * self.altura
        return area

ac = Cuadro.calcular_area(0,1,2)
print ac
