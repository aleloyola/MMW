import ConfigParser
from datetime import datetime
from JsonController import JsonController
from RestController import RestController

request = RestController()
jsoncontrol = JsonController()

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
print(URI)
response = request.get(URI)


token = response[0]['Token']

URI_ventas = url_ventas+token+params_venta
response_venta = request.get(URI_ventas)

print(token)
print(response_venta)

jsoncontrol.writefile(file_name, response_venta)

#print ()
#for driver in response:
#    print (driver['EV_VENTA'])
