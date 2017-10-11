
# ########################################################################
# import time
# import webbrowser
#
# total_B = 3
# Break_C = 0
#
# print ("This program started on " + time.ctime())
# while Break_C < total_B:
#     time.sleep(2)
#     webbrowser.open_new("www.youtube.com")
#     Break_C = Break_C + 1

#######################################################################
# for y in range(1,11):
#     for x in range(1,11):
#         Resultado = x * y
#         print(x, "x", y, "=",Resultado)

########################################################################
#Funciones REcursivas

def play(intento=1):
    respuesta = input("De que color es la naranja? ")
    if respuesta != "naranja":
        if intento < 3:
            print("\nFallaste! Intentalo de nuevo")
            intento += 1
            play(intento) #llamada recursiva
        else:
            print ("\nPerdiste")
    else:
        print ("\nGanaste")

play()




#file = open('lorem ipsum.txt','w')
#file.write('lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum')
#file.close()


#Lista = [1,2,3,4,5,6]

#print (Lista[2])
#print (Lista[2:5])
#print (Lista[5:])
#print (Lista[:5])
#print (Lista[:])

#Lista = [1,2,3,4,5,6]
#def recorre_lista(Lista):
#    m = 0
#    for i in range(len(Lista)):
#        if m < Lista[i]:
#            m = Lista[i]
#            print (i,m)

#recorre_lista(Lista)
#################################
#PARA AGREGAR ELEMENTOS SE USA.append
#append es al fina de la lista
#videojueagos.insert(2,fifa 2019)
#print video juego





#.idex(i)

#Videojuegos.pop()
#quita al final por defecto pero tambie se puede con indice

#lista.remove(1) quita por nombre

#############################################################
#def Crear_Lista ():
#    N = int(input("que numero de Palabras deseas?"))
#    if N >= 1:
#        print (N)
        #for N range(1,N)
        #L = input("Escribe Palabra")
        #L = L + 1
#    print(N)
#Crear_Lista()
######################################################################3
#numero = int(input("Numero de Palabras?"))
#if numero < 1:
#    print("Imposible")
#else:
#    lista = []
#    for i in range(numero):
#        print("Pon Palabras", str(i+1) + ":")
#        palabra = input()
#        lista.append(palabra)
#    print(" La Lista es:", lista)
########################################################################

#for y in range(1,11):
#    for x in range(1,11):
#        Resultado = x * y
#        print(x, "x", y, "=",Resultado)

#print ("\t\t".join(map(lambda x: "".join(raw_input("Dame uno elemento\t\t")) ,range(input("Dame tamanio de la lista: \t")))))


#    m = 0
#    for i in range(len(Lista)):
#        if m < Lista[i]:
#            m = Lista[i]
#            print (i,m)


#Escribir programa que valide dir ip 000.000.000.000
#ip[]
#ip = input("Inserta Direccion IP")
#if len(ip) >=12 ant type(ip)
#    print ip

# ip = input("Insert IP: ")
#
# if len(ip)>=15 and len(ip)<=15:
#     ip_tex = ip.split('.')
#        if ip_text =
#     print("ip Invalido")
#     print (ip)
#     print ("IP Correcto")
# else:
#     print("ip Invalido")


############################################################################################

# def Dist_euc ():
#     n1 = 0
#     n2 = 0
#     d = 0
#     n1 = int(input("X 1 : "))
#     n2 = int(input("Y 1 : "))
#     n3 = int(input("X 2 : "))
#     n4 = int(input("Y 2 : "))
#     if n1 >= 0 and n2 >= 0:
#         if n3 >= 0 and n4 >= 0:
#             print("(",n1, ",", n2, ")(", n3,",",n4,")")
#             d = (((n1 - n3) ** 2) + ((n2 - n4) ** 2)) ** .5
#             print(d)
#
#
#     else:
#          print("ERROR")
#
#
# Dist_euc ()


##############################################################################################33

#HORA CAMBIO A FORMATO AM / PM
# def horario():
#
#     hora_f = ""
#     hora_i =input("Pon la hora en formato 00:00:00 ")
#     hr = int(hora_i[0]+hora_i[1])
#     #print_HR
#     if hr < 12:
#         hora_f += (hora_i , " AM")
#     else:
#         hr = hr - 12
#         hora_f = str(hr)
#         hora_f += (":" + hora_i[3:] + " PM")
#     print(hora_f)

    # h24 = int(input("Introduce Hora: "))
    # m24 = int(input("Introduce Minutos: "))
    # if h24 > 12:
    #     h24 = h24 - 12
    #     print(h24,":",m24,"PM")
    # else:
    #     print(h24, ":", m24, "AM")

# horario()


# ###########################################################
# Lista = [1,2,3,4,5,6]
#
# print (Lista[2])
# print (Lista[2:5])
# print (Lista[5:])
# print (Lista[:5])
# print (Lista[:])
#
# Lista = [1,2,3,4,5,6]
# def recorre_lista(Lista):
#    m = 0
#    for i in range(len(Lista)):
#        if m < Lista[i]:
#            m = Lista[i]
#            print (i,m)
#
# recorre_lista(Lista)

#############################################################################
