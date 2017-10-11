#Encoding
# -*- coding: utf-8 -*-
import json

class data(object):

    def __init__(self, data):
        self.results = data['data']

    def imprimir_data(self):
        resultado = results(self.results)
        resultado.impirmir_results()


class results(object):

    def __init__(self, results):
        self.thumbnail = results['results']

    def impirmir_results(self):
        comic = comics(self.thumbnail)
        comic.imprimir_results()

class comics(object):

    def __init__(self , comics):
        self.snchanges = comics
        self.comics_init = comics[0]["comics"]

    def imprimir_results(self):
        itemsa = items(self.comics_init)
        itemsa.cuantos_elementos_comics()
        series(self.snchanges[0]["series"])

class items(object):

    def __init__(self, items):
        self.items_init = items
        self.lista = []

    def cuantos_elementos_comics(self):
        self.avaliable = self.items_init["available"]
        self.recorrer_array()

    def recorrer_array(self):
        for y in self.items_init['items']:
            self.lista.append(y['name'])
        print self.lista

class series(object):

    lista = []

    def __init__(self, items):
        self.series = items["items"]
        self.recorrer_array()

    def recorrer_array(self):
        for d in self.series:
            self.lista.append(d['name'])
        print self.lista


class main(object):
    json_file = open("C:/Users/GustavoMahatma/Desktop/marvel.json").read()
    json_data = json.loads(json_file)
    infodata = data(json_data)
    infodata.imprimir_data()


mainshow = main()