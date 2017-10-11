import requests
import json

#lat-33.86755700000001 log 151.201527
def pedir_data():

    latitud = input("introduce Latitud")
    longitud = input("introduce Longitud")

    url = ('https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='+ latitud + ',' + longitud + '&radius=500&type=restaurant&keyword=cruise&key=AIzaSyBSa0SUjt7GVytZzWuzp32_nbby0RNBoNE')#, auth=('user', 'pass'))

    print(url)
    response = requests.get(url)
    json_objet_response = response.json()
    print(response.json())

class PlacesResponses(object):

    def __init__(self,place_objetct_response):
        self.__place_objetc_response = place_objetc_response
        self.json_objets

    #json_file = open(''.read())

    #json_data = json.loads(json_file)
pedir_data()








# print (r.status_code)

####parcear