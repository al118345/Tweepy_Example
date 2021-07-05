# Cómo obtener y almacenar en un documento .csv Tweets sobre una temática


## Introducción

En este proyecto vamos a generar una pequeña investigación desde el punto de vista del Big Data y de las redes sociales. Exactactamente, hemos utilizado Twitter como fuente textual, una red social en la que se pueden recolectar datos de forma más sencilla y, sobre todo, inmediata, necesario para establecer correlaciones temporales entre la evolución del virus y la opinión del mismo  de la sociedad.

Esta plataforma permite el envío de mensajes en texto plano de corta longitud por parte de los usuarios, con un máximo de 280 caracteres. Estos mensajes, llamados tweets, se muestran en la página principal del usuario y pueden ser capturados a través de una API proporcionada por la propia red social.

Este ejemplo va a consistir en la implementación de un script en Python que almacene continuamente todos los tweets que se escriben sobre el Coronavirus en español.

El código esta explicado en la url https://1938.com.es/app-coronavirus-twitter

### Files

En este repositorio se pueden encontrar los siguientes ficheros:

* **Tweepy.py** Este fichero recoge el código que ejecuta la recogida de  tweets a través de una consulta.
  
* **Tweepy_Listener.py** Este fichero recoge el código que ejecuta un Listener encargado de ir almacenado continuamente todos los tweets sobre una temática.
  
* **Tweepy_ejemplo_localizacion.py** Este fichero recoge el código que ejecuta un Listener encargado de ir almacenado continuamente todos los tweets con información sobre su geolocalización. Más información https://1938.com.es/tweets_geolocalizados.

* **autenticate_example.py**  Este archivo es un fichero auxiliar donde se referencian las credenciales para acceder a la API de Twitter y obtener los tweets.

* **requirements.txt** Este archivo menciona los paquetes Python necesarios para ejecutar el código.

### Prerequisites

```
twint
tweepy
pandas
```

### Installing
Para ejecutar este proyecto es necesario ejecutar el siguiente comando y añadir las credenciales de acceso a la api de twitter. 

```
python get-pip.py install -r requirements.txt
git clone --depth=1 https://github.com/twintproject/twint.git
cd twint
python get-pip.py  install . -r requirements.txt
```
o en el caso de linux

```
pip install -r requirements.txt
git clone --depth=1 https://github.com/twintproject/twint.git
cd twint
pip3 install . -r requirements.txt
```

## Authors
* Rubén Pérez Ibáñez

## License
Released Under CC BY-SA 4.0 License

