import twint
'''

# Configure buscamos todos los tweets emitidos por nosotros en angular.
c = twint.Config()
c.Username = "1938web"
c.Search = "Angular"

# Ejecutamos la búsquedas.
twint.run.Search(c)

'''
# Segunda consulta.
c = twint.Config()
# Buscamos un usario
# Buscamos el término que aparezca.
c.Search = "spain"
#almacenamos la búsquead en un documento csv.
c.Store_csv = True
# escoge el nombre del fichero.
c.Output = "futbol.csv"
twint.run.Search(c)
