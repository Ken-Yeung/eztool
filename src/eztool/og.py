import traceback #traceback.print_exception(*sys.exc_info())
import sys
from datetime import datetime
import pytz

# Datetime
def t_now(timezone:str = "Hongkong", time_fmt: str = "%d/%m/%Y %H:%M:%S"):
    """Getting Time with default format %d/%m/%Y %H:%M:%S and default timezone is Hongkong."""
    hk_tz = pytz.timezone(timezone)
    return datetime.now(hk_tz).strftime(time_fmt)
# Datetime

class lst_handler:
    def __init__(self, data):
        self.table = data
        pass

    def get_row(self, x):
        row = self.table[x-1]
        return row

    def get_column(self, y):
        re_lst = []
        for i in self.table:
            cell = i[y-1]
            if cell != None and cell != '':
                re_lst.append(cell)
        return re_lst

    def get_cell(self, x, y):
        return self.table[x-1][y-1]

# if __name__ == "__main__":
#     print(t_now())