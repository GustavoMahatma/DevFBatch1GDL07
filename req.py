import requests


x = input('Quieres sugerencias de Peliculas o Musica, pon alguna de tu gusto: \n')
y = input('Ecribe otra pelicula o Musico: \n')

consulta = x + ', ' + y

parametros = {'k': '286940-DevFSens-0KCM0XSU', 'q': consulta}

url = 'https://tastedive.com/api/similar?'
respuesta = requests.get(url, params = parametros)

print(respuesta.url)

json_objets_respuesta = respuesta.json()

print (json_objets_respuesta)

a = json_objets_respuesta['Similar']['Info'][0]
b = json_objets_respuesta['Similar']['Info'][0]['Type']

lista_a = []
for x in range (0,19):
    c = json_objets_respuesta['Similar']['Results'][x]['Name']
    lista_a.append(c)
    print(c)
print(lista_a)

for x in range(len(lista_a)):
    print(lista_a[x])

print(a)
print(b)
data = json_objets_respuesta
resultsall = data['Similar']['Results']
Results(resultsall)

class Results(object):
    lista = []

    def __init__(self, results):
        self.results = results
        for x in range(len(self.results)):
            self.lista.append(self.results[x])
        name(self.lista)


# class Similar():
#     def__init__(self):
#     pass
#
# class Info():
#     pass

# git
# Github



