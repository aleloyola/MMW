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
url = config.get('API', 'API.url')
header_property = config.get('API', 'API.header_property')
header_value = config.get('API', 'API.header_value')
file_name = config.get('file', 'file.download_file_name') + datetime.now().__str__() + '.json'

response = request.get(url, header_property, header_value)
jsoncontrol.writefile(file_name, response)


print (response[0]['first_name'])
for driver in response:
    print (driver['first_name'])
