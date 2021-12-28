import requests
import json

from .. import info

api_name = "MOJANG API"
headers = {'User-Agent': str(info.PACKAGE_NAME)}
error_format = f"\u001b[33m{api_name}" + ": [{}] {}\u001b[0m"

class MojangAPIError(Exception):
    pass

def request(url:str): #Makes request to api then returns data in json
    #Make request.
    response = requests.get(url, headers=headers)
    data:dict = response.json()
    
    try: #Nova Universe API error catcher.
        error = data["error"]
        message = data["errorMessage"]

        raise MojangAPIError(f"{api_name}: [{error}] {message}")
    except KeyError:
        pass

    return data