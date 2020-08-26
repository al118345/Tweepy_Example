import tweepy
import csv #Import csv
# import libraries
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd
from datetime import date, datetime
import os
from autenticate import get_auth



'''
Código base para la obtención de los tweets. 
'''

def almacenar_tweet( status):
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





if __name__ == '__main__':
    print("===== Captador de tweets =====")
    # Get an API item using tweepy
    auth = get_auth()  # Retrieve an auth object using the function 'get_auth' above
    api = tweepy.API(auth)  # Build an API object.

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

                ]
                csvWriter.writerow(cabecera)
                csvFile.close()
                print("Creación de la cabecera")

    start_date = datetime(2019, 9, 19, 12, 00, 00)
    end_date = datetime(2020, 4, 19, 13, 00, 00)

    for tweet in tweepy.Cursor(api.search, q="Coronavirus" ,
                                       lang="es",
                                       since=start_date ,until= end_date ).items():
                print(tweet.created_at, tweet.text)
                almacenar_tweet(tweet)


    # End
    print("Terminado")



