import traceback #traceback.print_exception(*sys.exc_info())
import sys
import json

class json_worker:
    def __init__(self, path):
        self.file_path = path
        pass

    def read(self):
        with open(self.file_path) as json_file:
            data = json.load(json_file)
        return data

    def write(self, obj):
        with open(self.file_path, "w") as json_file:
            json.dump(obj, json_file)
        return True