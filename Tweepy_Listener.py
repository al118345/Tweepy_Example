import tweepy
import csv #Import csv
# import libraries
import time
import pandas as pd
from datetime import date
import os


from autenticate import get_auth


'''
Código base para la obtención de los tweets. 
'''
class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
            csvFile = open('result.csv', 'a', newline='')
            csvWriter = csv.writer(csvFile)
            if status is not False and status.text is not None:
                try:
                    texto = status.extended_tweet["full_text"]
                except AttributeError:
                    texto = status.text
                print(texto)
                linea = [status.created_at,
                         status.id, texto, status.source, status.truncated,
                         status.in_reply_to_status_id, status.in_reply_to_user_id,
                         status.in_reply_to_screen_name, status.geo, status.coordinates,
                         status.place,status.contributors, status.lang, status.retweeted]
                linea = linea
                csvWriter.writerow(linea)
            print("Almacenamos Tweet")
            csvFile.close()
            print("fin")

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
                    'result.csv'):
               print('Preparado el fichero')
            else:
                print('El no archivo existe.');
                csvFile = open('result.csv', 'w', newline='')
                csvWriter = csv.writer(csvFile)
                cabecera=['Fecha_creación','Id','Texto','Fuente','Truncado'
                    ,'Respuesta_al_tweet','Respuesta_al_usuario_id'
                    ,'Respuesta_al_usuario_nombre'
                    ,'Localización'
                    ,'Coordenadas'
                    ,'Ciudad'
                    ,'Contribuciones'
                    ,'Idioma'
                    ,'Retweeted'

                ]
                csvWriter.writerow(cabecera)
                csvFile.close()
                print("Creación de la cabecera")
            myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
            print(">> Listening to tweets about #coronavirus en castellano:")
            myStream.filter(track=['Coronavirus'], languages=['es'])
        except:
            continue
    # End
    print("Terminado")
