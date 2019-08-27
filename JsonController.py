import json


class JsonController:
    def __init__(self):
        pass

    # instance method
    def writefile(self, filename, jsonfile):
        with open(filename, 'w') as json_file:
            json.dump(jsonfile, json_file)
