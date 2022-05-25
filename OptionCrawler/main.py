# Created by Ken Yeung

# pip install -r requirements.txt
from pandas_datareader import data
from datetime import date
from openpyxl import load_workbook
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import sys
import traceback
from bs4 import BeautifulSoup
from time import sleep
import math
import xlwings as xw
import numpy as np

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

def closest_p(price,lst, units): # not perfect in 3rd arg | units == 3 must work
    assert units <= len(lst)
    result = min(lst, key=lambda x:abs(x-price))
    sort = sorted(lst)
    close_lst = []
    close_pos = ""
    for i, data in enumerate(sort):
        if data == result:
            close_pos = i
            break
    
    if close_pos == 0:
        close_lst = sort[:units]
            
    elif close_pos == len(sort)-1:
        close_lst = sort[-(units):]

    else:
        devided = units/2
        foo = math.floor(devided)
        if units > 6:
            foo = foo + 1
        close_lst = sort[close_pos-foo:close_pos+math.ceil(devided)]
    
    return close_lst

class xw_table:
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
            self.excel.save()
            return True
        except Exception as e:
            traceback.print_exception(*sys.exc_info())
            return False

    def clear_row(self, sht, max_row):
        shit = self.excel.sheets[str(sht)]
        self.excel.save()
        return False

def getoctstockprice(stock):
    start = date(2021,10,4)
    end = date(2021,10,4)
    p = data.DataReader(stock, 'yahoo', start, end)
    pk = p['Close'].values[0]
    return pk

def set_stock_price(cell, xl_location, sht):
    start_cell = cell
    local_excel = xw_table(xl_location)
    local_table = local_excel.get_table(sht, start_cell)

    for i, code in enumerate(local_table):
        if i > 0: # Must Skip Title
            count = 0
            while True:
                try:
                    if count < 11:
                        price = getoctstockprice(code[0])
                    else:
                        price = "Data not found"
                    break
                except Exception as e:
                    count = count + 1
                    print(f"{code[0]} Error: retrying...{str(count)}")
                    print("="*72)
            print(f"{str(i)}) Stock: {code[0]} | Price: {price}")
            local_table[i][2] = str(price)
            local_excel.set_table(sht, start_cell, local_table)
    print("Data saved.")
    return False

def option(driver, stock):
    table = []
    url = f"https://www.hkex.com.hk/market-data/futures-and-options-prices/single-stock/details?sc_lang=en&product={stock}"

    driver.get(url)
    delay = 60 # seconds
    try:
        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, "option")))
        print("Page is ready!")
        sleep(1.2)
    except TimeoutException:
        print("Loading took too much time!")

    raw_table = driver.find_element_by_id("option")
    soup = BeautifulSoup(raw_table.get_attribute('innerHTML'), "html.parser")

    for i, row in enumerate(soup.find("tbody").findAll("tr")):
        data_lst = []
        for ii, data in enumerate(row.findAll("td")):
            data_lst.append(data.text)
        table.append(data_lst)
    return table

def into_excel(excel, sht, start, details):
    xl = xw_table(excel)
    table = xl.get_table(sht, start)
    table = xl.get_table(sht, start)
    a = np.array(table)
    if len(a.shape) < 2:
        table = [table]

    table.append(details)
    xl.set_table(sht, start, table)
    return False

def main(price_start_cell, excel, stock_price_sht, option_sht, webdriver_chrome_path):
    set_stock_price(price_start_cell, excel, stock_price_sht)

    stock_info_table = xw_table(excel)
    needed_tinfo = stock_info_table.get_table(stock_price_sht, price_start_cell)

    driver = webdriver.Chrome(webdriver_chrome_path)

    for i, data in enumerate(needed_tinfo):
        if i > 0:
            print(f"Stock option: {data[1]}")
            op_table = option(driver, data[1])
            foo_lst = []
            for ii in op_table:
                call_bid = ii[3].split("/")[0]
                put_bid = ii[7].split("/")[0]
                strike = ii[5]

                op_lst = [
                    data[0],
                    data[1],
                    data[2],
                    call_bid,
                    strike,
                    put_bid
                ]

                foo_lst.append(op_lst)

                print(f"Call bid: {call_bid} | Strike price: {strike} | Put bid: {put_bid}")
                print("-"*72)
            
            lst_worker = lst_handler(foo_lst)
            strike_col = [float(i) for i in lst_worker.get_column(5)]
            try:
                closet = closest_p(float(data[2]), strike_col, 3)

                pos_lst = []
                for pos, sti in enumerate(foo_lst):
                    for foo_sti in closet:
                        if float(sti[4]) == foo_sti:
                            pos_lst.append(sti)

                print("="*72)
                print(f"Price: {data[2]}")
                print(closet)
                print("="*72)
                for damn in pos_lst:
                    print(damn)
                    into_excel(excel, option_sht, price_start_cell, damn)
                print("Added data")
            except Exception as e:
                traceback.print_exception(*sys.exc_info())
                pass

    # input()
    driver.close()
    return False
##########################################! Edit below !##########################################
if __name__ == "__main__":
    price_start_cell = "A1"
    excel = "stock_list.xlsx"
    stock_price_sht = "data"

    option_sht = "strike"
    webdriver_chrome_path = "driver/win_chromedriver.exe" # './mac_chromedriver'
    main(price_start_cell, excel, stock_price_sht, option_sht, webdriver_chrome_path)
    print("="*33, end="All Finished")
    print("="*33)