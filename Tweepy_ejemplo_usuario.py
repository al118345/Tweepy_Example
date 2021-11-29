import tweepy
import csv
from datetime import date, datetime
import os
from autenticate import get_auth

def almacenar_tweet(status):
    csvfile = open('pfizer.csv','a',newline='')
    csvwriter = csv.writer(csvfile)
    if status is not False and status.text is not None:
        try:
            texto = status.extended_tweet["full_text"]
        except AttributeError:
            texto = status.text
        print(texto)

        linea =[texto, status.truncated]
        linea = linea
        csvwriter.writerow(linea)
    print("Almacenamos Tweet")
    csvfile.close()
    print("fin")


if __name__ == '__main__':
    print("Extractor de Tweets")
    auth = get_auth()
    api = tweepy.API(auth)

    if os.path.isfile(
        'pfizer.csv'):
        print("Preparando el fichero")
    else:
        print("No existe el fichero")
        csvFile = open('pfizer.csv', 'w',newline='')
        csvWriter = csv.writer(csvFile)
        cabecera=['Texto', 'Truncado']
        csvWriter.writerow(cabecera)
        csvFile.close()
        print("Se creo el header")

    start_date = date(2020, 12, 24)
    end_date = date.today()
    tweets = []

    for tweet in tweepy.Cursor(api.search_tweets, "pfizer sintomas",
                             ).items():
        if tweet.created_at.date() < end_date and tweet.created_at .date()> start_date:
            if tweet.text not in tweets:
                tweets.append(tweet)
                almacenar_tweet(tweet)

print("Terminado")