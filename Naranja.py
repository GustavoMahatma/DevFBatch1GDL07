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
