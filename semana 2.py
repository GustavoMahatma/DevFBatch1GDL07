# Encoding
# -*- coding: utf-8 -*-
# my_set={1,3}
#
# def add_element_to_set():
#     my_set.add(2)
#     print('element',my_set)
#     my_set.update([2,3,4])
#
#     print('Elementos:',my_set)
#
#     my_set.update([4,5],{1,6,8})
#
#     print('Elem:',my_set)
#
#     my_set2={1,3,4,5,6}
#     print('set2',my_set2)
#
#     my_set2.discard(4)
#     print('set2', my_set2)
#
#     my_set3=set('HelloWorld')
#     #desordena la lista
#     print(my_set3)
#
#     #Pop random elementos
#     my_set3.pop()
#     print(my_set3)
#
#     my_set3.clear()
#
#
#     print(my_set3)
# add_element_to_set()


# my_set = set("Hellow World")
#
# set.upddate
# set.remove()
# set.discard()
#
# print(my_set.pop())
#
# set = {2,0}
#
# def pop_element_from_set():
#     #Iniciar mi set
# #Output: set of unique elemeents
# my_set = set( "Hellow World")
# print(my_set)

# A = {1,2,3,4,5}
# B = {4,5,6,7,8}
#
# y = set.intersection(A,B)
# x = set.union(A,B)
# print("I: ", y, "- U: ",x)
#
# inter = A.intersection(B)
# print ("I: ",inter)
#
# my_tuple = (1,"Hello",3,4)

# def cambiando_elemento():
#     my_tuple = (4,2,3,[6,5])
#     my_tuple[3][0] = 9
#     print (my_tuple)
#
# cambiando_elemento()

# TUPLAS
# def creando_tuplas():
#     # empty tuple
#     my_tuple = ()
#     print(my_tuple)
#
#     # tuple having integers
#     my_tuple = (1, 2, 3)
#     print(my_tuple)
#
#     # tuple with mixed datatypes
#     my_tuple = (1, "Hello", 3.4)
#     print(my_tuple)
#
#     # nested tuple
#     my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
#     print(my_tuple)
#
#     # tuple can be created without parentheses
#     # also called tuple packing
#
#     my_tuple = 3, 4.6, "dog"
#     print(my_tuple)
#
#     # tuple unpacking is also possible
#     a, b, c = my_tuple
#     print(a)
#     print(b)
#     print(c)
#
# # creando_tuplas()
#
# def indexing_tuplas():
#     my_tuple = ('p', 'e', 'r', 'm', 'i', 't')
#
#     # Output: 'p'
#     print(my_tuple[0])
#
#     # Output: 't'
#     print(my_tuple[5])
#
#     # index must be in range
#     # IndexError: list index out of range
#
#     # print(my_tuple[6])
#
#     # index must be an integer
#     # TypeError: list indices must be integers, not float
#
#     # my_tuple[2.0]
#
#     # nested tuple
#     n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
#
#     # nested index
#     # Output: 's'
#     print(n_tuple[0][3])
#
#     # nested index
#     # Output: 4
#     print(n_tuple[1][1])
#
# # indexing_tuplas()
#
# def cambiando_elementos():
#     my_tuple = (4, 2, 3, [6, 5])
#
#     # we cannot change an element
#     # TypeError: 'tuple' object does not support item assignment
#
#     my_tuple[1] = 9
#
#     # # but item of mutable element can be changed
#     # my_tuple[3][0] = 9
#     # print(my_tuple)
#     #
#     # # tuples can be reassigned
#     # my_tuple = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
#     # print(my_tuple)
# cambiando_elementos()

#Diccionarios
# JSON java s
# XML
# SOAP
# GRAP,QL
# API REST
#
# def accesar_elementos():
#     my_dict ={'name': 'Jack','Age':26,'Address':'Rosal# 234'}
#     print(my_dict['name'])
#     print(my_dict.get('Age'))
#     print(my_dict['Address'])
#     x = my_dict
#     print(x)
#
# accesar_elementos()
#
# square.pop[4]
# square.popitem()
#
# del square [5]

# square ={x: x* x for x in range (6)}
# print(squares)
#
# como
# squares = {}
# for x in range(6):
#     squares[x] = x * x
#     print(x)
#     print(squares)

# Guardar en la lista los numeros divisibles entre 7
# pero no multiplo entre 5, desde 2000 : 3200 imprimir lista separada por comas

# familia = {'Miembros':('Karla','Elisa','Gustavo','Valentina'),'Edad':('25','3','30','7'),'Cumple':('12 Dic','14 Abr', '04 Oct', '19 Abr')}
# print(familia)
#
# item%7 == 0
# item%!= 0
#
# numeros = {}
# for x range(2000,3200)
#       item%7 == 0
#        item%5!= 0
#     squares[x] = x * x
#     print(x)
#     print(squares)

################################################################################################
# import os
# def nombre():
#
#     #lista_ok = os.getcwd("C:\Users\GustavoMahatma\PycharmProjects\First\Prank")
#     lista_nombres = os.listdir("C:\prank")
#     print(lista_nombres)
#     num_file = len(lista_nombres)
#     print(num_file)
# #     for y in (lista_nombre):
# #         #print(lista_nombres[y]," % ")
# #         print(y)
# #         #os.chdir("C:\prank")
# #         print(os.rename(lista_nombres[y],lista_nombres[y].translate(None, "012456789")))
# # nombre()
# #
# #         #lista_nombres[y].translate(None,0,1)
# #         #os.renames(lista_nombres[y], new_name)
#
#     # for x range (1,45):
#     #     print(x)
#          new_name = lista_nombres[x].translate(None,"012456789")
#
    #     os.renames(lista_nombres[x],new_name)
    #     print(new_name)

    #os.rename(old,)
    #os.chdir("dir") cambio de ruta
    #"08nombre.foto".translate(None,)

#String.translate()
#change_name()
# for y in range(1,11):
#     for x in range(1,11):
#         Resultado = x * y
#         print(x, "x", y, "=",Resultado)



# import os
# from datetime import datetime
#
# ruta_app = os.getcwd("C:\Users\GustavoMahatma\Desktop\FAUSTO VINTAGE")  # obtiene ruta del script
# contenido = os.listdir(ruta_app)  # obtiene lista con archivos/dir
# total = 0
# archivos = 0
# formato = '%d-%m-%y %H:%M:%S'  # establece formato de fecha-hora
# linea = '-' * 40
#
# for elemento in contenido:
#     archivo = ruta_app + os.sep + elemento
#     if not os.access(archivo, os.X_OK) and os.path.isfile(archivo):
#         archivos += 1
#         estado = os.stat(archivo)  # obtiene estado del archivo
#         tamaño = estado.st_size  # obtiene de estado el tamaño
#
#         # Obtiene del estado fechas de último acceso/modificación
#         # Como los valores de las fechas-horas vienen expresados
#         # en segundos se convierten a tipo datetime.
#
#         ult_acceso = datetime.fromtimestamp(estado.st_atime)
#         modificado = datetime.fromtimestamp(estado.st_mtime)
#
#         # Se aplica el formato establecido de fecha y hora
#
#         ult_acceso = ult_acceso.strftime(formato)
#         modificado = modificado.strftime(formato)
#
#         # Se acumulan tamaños y se muestra info de cada archivo
#
#         total += tamaño
#         print(linea)
#         print('archivo      :', elemento)
#         print('modificado   :', modificado)
#         print('último acceso:', ult_acceso)
#         print('tamaño (Kb)  :', round(tamaño / 1024, 1))
#
# print(linea)
# print('Núm. archivos:', archivos)
# print('Total (kb)   :', round(total / 1024, 1))



#queues =  deque([])
# stack = [3,4,5]
# stack.append(6)
# stack.append(7)
# print(stack)
# #out
# [3,4,5,6,7]
# stack.pop()
# 6
#
# algoritmos
# binary.search
# divide and Conquer
# pick.search
#
# logaritmos

# import os
# path = ("/prank")
# os.chdir(path)
#
# def rename_file():
#     dirs = os.listdir("/prank")
#     lista_nombres = []
#
#     print(dirs)
#     os.chdir("/prank")
#     num = "0,1,2,3,4,5,6,7,8,9"
#     for i in (dirs):
#         #print (i.translate(None, num))
#         temp = i.translate(None, num)
#         os.rename(i, temp)
#     dirs = os.listdir("/prank")
#     print(dirs)
#
#
# rename_file()


# import os
# path = ("/prank")
# os.chdir(path)
#
# def rename_files():
#     #(1) get names from  th folder
#     file_list = os.listdir("/prank")
#     print (file_list)
#     saved_path = os.getcwd()
#     print("Current Working Directory is:"+ saved_path)
#     os.chdir("/prank")
#     #(2) for each file, Change the name
#     for file_name in file_list:
#         os.rename(file_name, file_name.translate(None, "0123456789"))
#
#     os.listdir(saved_path)

#rename_files()

# def fu_suma(x,y):
#     #algoritmo
#     return x+y
#
# suma = fu_suma(2,4)
# print(suma)
#
# for x in range(1,3):
#     mulsum= fu_suma(x,x)
#     print(mulsum)
#
# #API
#
# #Parametro
# def mi_fun(message)
#     message = "Hola Mundo"

#ATOM....editor de texto

#Escriba un rpograma que permita crear una lista de palabras.
# para ello, el programa tiene que pedir un numero y luego solicitar ese numero de palabras para  crear la
# lista . por ultimo, el programa tiene que escribir la lista

# def lista_palabras ():
#     lista = []
#     num_palabras = int(input("numero de palabras"))
#
#     for i in range(num_palabras):
#         lista.append(input("Palabra: \n"))
#
#     print(lista)
#
# lista_palabras()

# def buscar_en_lista():
#     list = ["Dog","Cat","Cat","Dog","Cat","Dog","Cat","Cat","Dog","Cat"]
#     x = input("Palabra a Buscar: \n")
#     y = 0
#     for i in range(len(list)):
#         if x == list[i]:
#             y = y + 1
#
#     print(y)
# buscar_en_lista()








# def lista_pal2():
#     list = []
#     n_p = int(input("Cuantas palabras?"))
#     while (len(list)) < (n_p):
#         list.append(input("introduce palabra:"))
#     print(list)
#
# lista_pal2()


# Python funtctional Programming
# def f(x):
#     return  x%3 == 0 or x%s ==0
# def filtrar():
#     print filter (f,range(2,25))


def f(x): return x % 3 == 0 or x % 5 == 0

print(filter(f,range(2,10000)))

# def cubo(x):
#     return x*x*x
# print(map(cubo,range(1,11)))

################EJEMPLO DE FUNCIONES ##################################################
# def regresa_valor():
#     print("Numeros que quieres sumar")
#     a=int(input("A:"))
#     b=int(input("B:"))
#     x = a + b
#     return x
#
# def imprime():
#     print(regresa_valor())
#
# def llamar_imprimir():
#     imprime()
#
# llamar_imprimir()

######################################################################################

# CamelCase
# Class Vehiculo:
# color=" "
#
# #metodo
# def acelerar():
# def frenar():
# def encender_apagar(Self,Status):
#
# car = Vehiculo()
# car.acelerar()
#
#
# def __init__(self,params)
#     sel.color = new_color


#
# Varaible
# , estancia es un objeto y el metodo es una accion