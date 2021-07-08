# encode : utf-8

import tweepy
import csv  # Import csv
# import libraries

import os
from autenticate import get_auth

'''
Código base para la obtención de los tweets. 
'''


class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):

        # if status is not False and status.text is not None and
        if status.coordinates is not None:
            try:
                texto = status.extended_tweet["full_text"]
            except AttributeError:
                texto = status.text
            texto = texto.replace('\n', '')
            print(texto)
            linea = [status.created_at,
                     status.id, texto, status.source, status.truncated,
                     status.in_reply_to_status_id, status.in_reply_to_user_id,
                     status.in_reply_to_screen_name, status.geo,
                     status.coordinates,
                     status.place, status.contributors, status.lang,
                     status.retweeted]


            csvFile = open('resultado_geolocalizado.csv', 'a', encoding= 'utf-8',  newline='')
            csvWriter = csv.writer(csvFile)
            csvWriter.writerow(linea)
            csvFile.close()
            print("Almacenamos Tweet")
        # print("fin")

    def on_error(self, status_code):
        print(status_code)
        return False


if __name__ == '__main__':
    print("===== Captador de tweets =====")
    # Get an API item using tweepy
    auth = get_auth()  # Retrieve an auth object using the function 'get_auth' above
    api = tweepy.API(auth)  # Build an API object.

    # Connect to the stream
    myStreamListener = MyStreamListener()
    while True:
        try:
            if os.path.isfile(
                    'resultado_geolocalizado.csv'):
                print('Preparado el fichero')
            else:
                print('El no archivo existe.');
                csvFile = open('resultado_geolocalizado.csv', 'w', encoding= 'utf-8', newline='')
                csvWriter = csv.writer(csvFile)
                cabecera = ['Fecha_creación', 'Id', 'Texto', 'Fuente',
                            'Truncado'
                    , 'Respuesta_al_tweet', 'Respuesta_al_usuario_id'
                    , 'Respuesta_al_usuario_nombre'
                    , 'Localización'
                    , 'Coordenadas'
                    , 'Ciudad'
                    , 'Contribuciones'
                    , 'Idioma'
                    , 'Retweeted'

                            ]
                csvWriter.writerow(cabecera)
                csvFile.close()
                print("Creación de la cabecera")
            myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
            myStream.filter(track=['Coronavirus'], languages=['en'])
        except:
            continue

    print("Terminado")