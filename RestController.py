import requests


class RestController:
    def __init__(self):
        pass

    header = ""
    url = ""

    # instance attribute
    # def __init__(self):

    # instance method
    def get(self, url, header_property, header_value):
        header = {header_property: header_value}
        response = requests.get(url, headers=header)
        if response.status_code != 200:
            # This means something went wrong.
            return "GET {} {}".format(url, response.status_code)

        return response.json()
