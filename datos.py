import json

class Data:
    def __init__(self, path):
        self.path = path
    
    def escribir_json(self, datos=[]):
        with open(self.path, 'w') as file:
            json.dump(datos, file, indent=4, ensure_ascii=False)
    
    def leer_json(self):
        try:
            with open(self.path, 'r') as file:
                data_from_json = json.load(file)
            
            return data_from_json
        except FileNotFoundError as err:
            print(err)
            self.escribir_json()

