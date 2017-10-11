# Encoding
# -*- coding: utf-8 -*-

#Variable Publico
#Variable Privado
#Metodos Publico
#Metodo Privado

# class Persona(object):
#
#     def __init__(self,nombre, email, age):
#         self.nombre = nombre
#         self.__email = email
#         self.__age = age
#
#     def get_name(self):
#         return self.nombre
#
#     def update_email(self, new_email): #"Actualizado en varibles privadas"
#         self.__email = new_email
#
#     def return_email(self):
#         return self.__email
#
#     def __show_age(self):
#         return self.__get_age()
#
#     def show_age(self):
#         return self.__get_age()
#
#     def __get_age(self):
#         return self.__age
#
#     #Sobrecarga de Metodos
#
#     def update_email(self,new_email, algo_mas):
#         self.__email = new_email + algo_mas
#
#
# tk = Persona('TK', 'tk@mail.com',25)
#
# print tk.return_email()

#Triangulo, Cuadrado y Circulo
#area = 0

class Figura(object):

    def __init__(self, valor_a):
        self.valor_a = valor_a

    # def calcular_area(self):
    #     return area


class Cuadro(Figura):

    def __init__(self, valor_a):
        super (self.valor_a).__init__(self, valor_a, valor_b)
        self.valor_b = valor_b

    def area_cuadro(self):
        area = self.valor_a * self.valor_b
        return area

class Circulo(Figura):

    def __init__(self, valor_a):
        super(self.valor_a).__init__(self,valor_a)

    def area_circulo(self):
        pi = 3.1416
        radio = (self.valor_a / 2)
        area = (radio*radio)  * pi
        return area

class Triangulo(Figura):

    def __init__(self, valor_a):
        super(self.valor_a).__init__(self, valor_a, valor_b)
        self.valor_b = valor_b


    def area_triangulo(self):
        area = (self.valor_a * self.valor_b) / 2
        return area

#
area_tri = Triangulo(3,4)
print area_tri.area_triangulo()

# area_c = Cuadro(3,4)
# print area_c.area_cuadro()
#
# area_ci = Circulo(4)
# print area_ci.area_circulo()





# tk = Persona('TK', 'tk@mail.com',25)
#
# print tk.return_email()