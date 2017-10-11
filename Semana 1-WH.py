#Encoding
# -*- coding: utf-8 -*-

# Kata #1
# Crea un programa que le pregunte al usuario su nombre y edad.
# Imprime un mensaje dirigido a él,
# que le diga el año en que cumplirá cien años
##########################################################################################################
# import time
#
# def Datos ():
#     y = time.ctime()
#     lista = [y]
#     print("Estamos en el Año",y[20:])
#     Anio = int(y[20:])
#     name = ""
#     name = input("Nombre: ")
#     edad = int(input("Edad: "))
#     a100 = ((100 - edad)+Anio)
#     print("Tu nombre es ",name,"Tienes ",edad ,"Años y Cumpliras 100 años el",a100)
#
# Datos()

##############################################################################################################

# #Encoding
# # -*- coding: utf-8 -*-
# import random
#
#
# def cuantosanosencien():
#     year = 2017
#     nombre = raw_input("¿Cual es tu Nombre? \n")
#     edad = int(raw_input("¿Cual es tu edad? \n"))
#     resultado_edad = 100 - edad
#     print nombre, "cumpliras 100 años en el año de", (year + resultado_edad)
#
#
# #cuantosanosencien()
#
#
# def par_o_impar():
#     numero = int(raw_input("¿Ingresa un numero porfavor? \n"))
#     if(numero%2==0):
#         print "Este es par"
#     else:
#         print "Este es impar"
#
#
# #par_o_impar()
#
#
# def crearListas_nuevas():
#     lista_preview = []
#     lista_init = []
#     lista_fin = []
#     for x in range(0,5):
#         lista_preview.append(int(raw_input("¿Ingresa un numero para ingresar a la lista? \n")))
#     for y in range(0, len(lista_preview)):
#         if(y == 0  or y == len(lista_preview)-1):
#             lista_init.append(lista_preview[y])
#         elif(y != 0 or y != len(lista_preview)-1):
#             lista_fin.append(lista_preview[y])
#
#     print "Lista de ultimo y primero ", lista_init
#     print "Lista de otros ", lista_fin
#
#
# #crearListas_nuevas()
#
#
# def es_igual_el_numero():
#     lista_all = []
#     for x in range(0,6):
#         lista_all.append(int(raw_input("¿Debes ingresar 6 numeros? \n")))
#     numero_rnd = random.randrange(0,5)
#     print lista_all
#     resultado_user = int(raw_input("¿Cual es el numero que ingresaste en la posicion " + str(numero_rnd) + "?"))
#     numero_colocado = lista_all[numero_rnd]
#     if resultado_user == numero_colocado:
#         print "El resultado es correcto le atinaste"
#     else:
#         print "Te la pelaste amiguito"
#
#
# es_igual_el_numero()


# Kata #2
# Pídele un número al usuario.
# Dependiendo de si el número es par o impar,
# imprime el mensaje apropiado al usuario

def par_o_impar():
    numero = int(input("Escribe Numero: \n"))
        if(numero%2==0):
        print("Este número es par" )
    else:
        print("Este número es impar" )



par_o_impar()












# Kata #3
# Escribe un programa que tome una lista de números
# (por ejemplo, a = [5, 10, 15, 20, 25]) y haz dos nuevas listas.
# una que contenga sólo el primer y último número de la lista original
# y otra que contenga todos los números intermedios
# Kata #4
# Escribe una función que tome una lista de números y un número.
# La función debe checar si el número pertenece a la lista y devolver
# el booleano correspondiente