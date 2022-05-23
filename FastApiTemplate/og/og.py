# Created by Ken Yeung
import codecs
import traceback #traceback.print_exception(*sys.exc_info())
import sys
import json
import pytz

# Datetime
def t_now(time_fmt: str = "%d/%m/%Y %H:%M:%S"):
    # time_fmt = "%d/%m/%Y %H:%M:%S"
    hk_tz = pytz.timezone("Hongkong")
    return datetime.now(hk_tz).strftime(time_fmt)
# Datetime

def html(page):
    html = codecs.open(f"web/html/{page}", "r").read()
    return html

def deliver(folder ,script):
    try:
        allow_list = json_worker("cdn_config.json")
        status: bool = script in allow_list.read()

        if not status:
            raise Exception

        cdn = codecs.open(f"web/{folder}/{script}", "r").read()
        return cdn

    except Exception as e:
        print("Requests: CDN Error")
        traceback.print_exception(*sys.exc_info())
        print("="*72)
        return "Bad requests"

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

def test(data)->str:
    # print(f"Hello {data}")
    res:str = f"Hello {data}"
    return res