# Encoding
# -*- coding: utf-8 -*-
#
# class Empleado():
#     monto_para_aumento = 1.04
#     numero_de_empleado = 0
#
#     def __init__(self, nombre, apellido, salario):
#
#         #self-< current intancece
#         self.nombre = nombre
#         self.apellido = apellido
#         self.email = nombre +"."+ apellido + "@company.com"
#         self.salario = salario
#
#         Empleado.numero_de_empleados += 1
#
#     # No olvidar escribir self cada que definamos un nuevo metodo
#
#     def nombre_completo(self):
#         return '{}{}'.format(self.nombre,self.apellido)
#
#     def obtener_salario(self):
#         return self.salario
#     def aplicar_aumento(self):
#         self.salario = int(self.salario * self.monto_para_aumento)
#
#     #print Empleado.numero_de_empleados
#
# empleado_1 = Empleado("Hugo","Melcaco",9000)
#
# print empleado_1

# MARCA TAMAÑO Y PRECIO
#
# CONTADOR DE PANTALLAS
#
# 5 atributos


class SmartTv():
    num_tv = 0
    iva = 1.16

    def __init__(self, marca, dims, precio, modelo, color):
        # self-< current intancece
        self.marca = marca
        self.dims = dims
        self.precio = precio
        self.modelo = modelo
        self.color = color

        SmartTv.num_tv += 1

    def tv_info(self):
        return 'Marca: {} Dims: {}  Precio:{}'.format(self.marca, self.dims, self.precio)

    def tv_iva(self):
        precio_miva = self.precio * self.iva
        return  precio_miva

# class Origen(SmartTv):
#     def __init__(self, marca, dims, precio, modelo, color, pais_org):
#         super(Origen, self).__init__(marca, dims, precio, modelo, color)
#         self.pais_org = pais_org
#         Origen.pais_org += 1
#
# class Fabrica(SmartTV,Origen):
#     def __init__(self, marca, dims, precio, modelo, color, pais_org, fabrica):
#         super(Origen, self).__init__(marca, dims, precio, modelo, color, pais_org)
#         self.fabrica = fabrica
#         Fabrica.fabrica += 1
#

num_tv_1 = SmartTv("Samsung","55 in.",14000,"MU55UHD","Negro")
# origen_1 = Origen("Samsung","49 in.",12000,"MU49UHD","Negro","Korea")
# fab_1 = Fabrica("Samsung","49 in.",12000,"MU49UHD","Negro","Korea","Seul 234")

print num_tv_1.color
print num_tv_1.modelo
print num_tv_1.tv_info()
print num_tv_1.tv_iva()

#print Pais()
# print Fabrica()