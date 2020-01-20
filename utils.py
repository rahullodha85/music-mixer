import json


class Helper:
    @staticmethod
    def read_input(file_name):
        with open(file_name, 'r') as file:
            text = file.read()
            return json.loads(text)

    @staticmethod
    def write_output(file_name, data):
        with open(file_name, 'w', encoding='utf-8') as file:
            json.dump(data, file)
