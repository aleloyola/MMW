import configparser
from datetime import date, timedelta
from JsonController import JsonController
from RestController import RestController
from MySQLController import MySQLController

request = RestController()
jsoncontrol = JsonController()
mysqlcontrol = MySQLController()
# reading property file
config = configparser.RawConfigParser()
config.read('ConfigFile.properties')

# reading properties values
url = config.get('API-login', 'API.url')
params = config.get('API-login', 'API.params')
file_name = config.get('file', 'file.download_file_name') + str(date.today()) + '.json'
url_ventas = config.get('API-ventas', 'API-ventas.url')
params_venta = config.get('API-ventas','API-ventas.params')
today = date.today()
yesterday = today - timedelta(1)
yesterday = str(yesterday)
today = str(today)
params_venta = params_venta.replace("DESDE",yesterday)
params_venta = params_venta.replace("HASTA", today)

URI = url + params
response = request.get(URI)
token = response[0]['Token']

URI_ventas = url_ventas+token+params_venta
print(URI_ventas)
response_venta = request.get(URI_ventas)
info_venta = response_venta[0]['ET_VENTA']

#Descomentar para apuntar a DB desarrollo
#host = config.get('mysql-desa', 'desa.host')
#user = config.get('mysql-desa', 'desa.user')
#password = config.get('mysql-desa', 'desa.password')
#db = config.get('mysql-desa', 'desa.database') 

#Descomentar para apuntar a DB producccion
host = config.get('mysql', 'prod.host')
user = config.get('mysql', 'prod.user')
password = config.get('mysql', 'prod.password')
db = config.get('mysql', 'prod.database')

mysqlcontrol.insertaventa(host, user, password, db, info_venta)

jsoncontrol.writefile(file_name, info_venta)


