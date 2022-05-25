<h1 align="center">:floppy_disk:<br>Welcome to Option Data Crawler</h1>

<div align="center">
<a herf="https://github.com/Ken-Yeung/KensToolkit.git"><img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="Python Badge"/></a>
<a herf="https://github.com/Ken-Yeung/KensToolkit.git"><img src="https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E" alt="JavaScript Badge"/></a>
<a herf="https://github.com/Ken-Yeung/KensToolkit.git"><img src="https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5 Badge"/></a>
<a herf="https://github.com/Ken-Yeung/KensToolkit.git"><img src="https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi" alt="FastAPI Badge"/></a>
</div>

>   $ python --version
>
>   Python 3.7.0

### Here's my creation workflow :receipt:

1.  [Instagram Auto Following Bot](https://github.com/Ken-Yeung/KensToolkit/tree/master/IgAutoFollow "Go to IgAutoFollow repo")
2.  [Option Data Crawler](#option-data-crawler-floppy_disk) <-- YOU ARE HERE
3.  [Link Tree](https://github.com/Ken-Yeung/KensToolkit/tree/master/LinkDistributor "Go to LinkDistributor repo")
4.  [File Transfer Server](https://github.com/Ken-Yeung/KensToolkit/tree/master/FilesTransferrer_one_direction "Go to FilesTransferrer_one_direction repo")
5.  [Api Initial Template](https://github.com/Ken-Yeung/KensToolkit/tree/master/FastApiTemplate "Go to FastApiTemplate repo")

-   [Back to Home Page](https://github.com/Ken-Yeung/KensToolkit "Home Page")

---

### Option Data Crawler :floppy_disk:

-   This script is crawling Hong Kong options' data using plugins `selenium` and `pandas_datareader`
-   Extract data from Yahoo Finance and HKEX into `stock_list.xlsx`
-   Extracting 3 options which strike price are closest to current stock price
-   Pulling data of call bid, put bid price and strike price
-   To extract specific company's stock, option data, you have to change the Row values of companies code in `stock_list.xlsx` sheet of `data`

1. Stock price would display in sheet: `data`
2. Option data would display in sheet: `strike`

### Usage:

-   Enter the command: `python3 main.py`

<!-- ### :exclamation::exclamation::exclamation: Notice :exclamation::exclamation::exclamation: -->

#### :bangbang: Notice :bangbang:

-   Chrome remote driver might not work if the version of that does not match the version of Chrome in local
-   This script only works in CPU format of AMD