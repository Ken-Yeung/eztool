import xlwings as xw

class xw_handler:
    def __init__(self, xl_name):
        self.excel = xw.Book(xl_name)
        pass

    def get_table(self, sht, start_cell):
        t_val = self.excel.sheets[str(sht)].range(str(start_cell)).expand("table").value
        return t_val

    def set_table(self, sht, start_cell, data):
        try:
            t_val = self.excel.sheets[str(sht)].range(str(start_cell)).expand("table")
            t_val.value = data
            return True
        except Exception as e:
            traceback.print_exception(*sys.exc_info())
            return False