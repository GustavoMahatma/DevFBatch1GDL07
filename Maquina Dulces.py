#2.5, 1.4, 4, 1.2
def iniciar():
    money = input("Cuanto dinero tienes? ")
    imprimirProductos(money)

def imprimirProductos(money):
    print ("\nLos dulces son:")
    dulces = ['Mazapan $2.5', 'Paleta Rosa $1.4', 'Algodon de Azucar $4', 'Cerveza $1.2']
    for dulce in dulces:
        print (dulce)
    dulcecito = input("\nQue dulce quieres? ")
    if dulcecito == ("Mazapan"):
        precio = 2.5
    elif dulcecito == ("Pan"):
        precio = 1.4
    elif dulcecito == ("Paleta"):
        precio = 4
    elif dulcecito == ("Chocolate"):
        precio = 1.2
    calcularVuelto(money, precio)

def calcularVuelto(monto, precioProducto):
    print ("Tu cambio es:")
    print (monto - precioProducto)
iniciar()