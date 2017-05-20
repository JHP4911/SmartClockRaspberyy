import json

class notes():

    def read(self):
        with open('notlar.json') as data_file:
            data = json.load(data_file)
        return data

    def write(self,data):
        with open('notlar.json', 'w') as outfile:
            json.dump(data, outfile)
