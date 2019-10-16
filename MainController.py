import ConfigParser
from datetime import datetime
from JsonController import JsonController
from RestController import RestController
from MySQLController import MySQLController

request = RestController()
jsoncontrol = JsonController()
mysqlcontrol = MySQLController()
# reading property file
config = ConfigParser.RawConfigParser()
config.read('ConfigFile.properties')

# reading properties values
url = config.get('API-login', 'API.url')
params = config.get('API-login', 'API.params')
file_name = config.get('file', 'file.download_file_name') + datetime.now().__str__() + '.json'
url_ventas = config.get('API-ventas', 'API-ventas.url')
params_venta = config.get('API-ventas','API-ventas.params')

URI = url + params
response = request.get(URI)
token = response[0]['Token']

URI_ventas = url_ventas+token+params_venta
print(URI_ventas)
response_venta = request.get(URI_ventas)
info_venta = response_venta[0]['ET_VENTA']

mysqlcontrol.insertData(info_venta)

jsoncontrol.writefile(file_name, info_venta)


