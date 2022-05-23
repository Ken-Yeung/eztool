# Created by Ken Yeung

import codecs
import io
import traceback #traceback.print_exception(*sys.exc_info())
import sys
import json
import pytz
import csv
from datetime import datetime
import glob

def glob_file():
    
    files = [f for f in glob.glob(f"database/*.csv")]
    # print(files)

    res = []
    for i in files:
        details = csv_worker(i).read()
        file_name = i.split("/")[1][:-4]
        # print(file_name)
        ios = 0
        android = 0
        for ii in details[1:]:
            if ii[1] == "ios":
                ios = ios + 1
            elif ii[1] == "android":
                android = android + 1

        # res[file_name] = {
        #     "count_ios": ios,
        #     "count_android": android,
        #     "total": len(details[1:]),
        #     "details": details[1:]
        # }

        res.append(
            {
                "month": file_name,
                "count_ios": ios,
                "count_android": android,
                "total": len(details[1:]),
                "details": details[1:]
            }
        )
    
    # for i in res:
    #     print(f"{i}: {res[i]}")

    return res

def recorder(data:str):
    head = [
        ['datetime', 'platform']
    ]

    fmt = "%d-%m-%Y %H:%M"

    current_datetime = t_now(fmt).split(" ")
    month_year = "_".join(current_datetime[0].split("-")[1:])
    # print(month_year)
    worker = csv_worker(f"database/{month_year}.csv")
    # worker.write(detail)
    new_row = [" ".join(current_datetime), data]
    try:
        origin = worker.read()
        origin.append(new_row)
        worker.write(origin)
    except:
        head.append(new_row)
        worker.write(head)
    return

# Datetime
def t_now(time_fmt: str = "%d/%m/%Y %H:%M:%S"):
    # time_fmt = "%d/%m/%Y %H:%M:%S"
    hk_tz = pytz.timezone("Hongkong")
    return datetime.now(hk_tz).strftime(time_fmt)
# Datetime

class csv_worker:
    def __init__(self, path) -> None:
        self.path = path
        pass

    def read(self) -> list:
        table = []
        result = []
        with open(self.path, "r") as details:
            table = csv.reader(details)
            result = [i for i in table]
        return result

    def write(self, table: list) -> None:
        with open(self.path, "w", newline='') as details:
            writer = csv.writer(details)
            writer.writerows(table)
        # print(f"Data wrote at: {self.path}")
        return

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