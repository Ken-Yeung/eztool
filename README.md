<h1 align="center">:confetti_ball:Welcome to Ken's Exhibition:tada:</h1>

<div align="center">
<a herf="https://github.com/Ken-Yeung/KensToolkit.git"><img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="Python Badge"/></a>
<a herf="https://github.com/Ken-Yeung/KensToolkit.git"><img src="https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E" alt="JavaScript Badge"/></a>
<a herf="https://github.com/Ken-Yeung/KensToolkit.git"><img src="https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5 Badge"/></a>
<a herf="https://github.com/Ken-Yeung/KensToolkit.git"><img src="https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi" alt="FastAPI Badge"/></a>
</div>

## Introduction :loudspeaker:

-   This repository is displaying some of the programs that I created and is displayable.
-   These programs' languages are mainly Python working with some JavaScript.
>   $ python --version
>
>   Python 3.7.0

### Here's my creation workflow :receipt:

1.  [Instagram Auto Following Bot](#instagram-auto-following-bot-robot)
2.  [Option Data Crawler](#option-data-crawler-floppy_disk)
3.  [Link Tree](#link-tree-evergreen_tree)
4.  [File Transfer Server](#file-transfer-server-card_index_dividers)
5.  [Api Initial Template](#api-initial-template-file_cabinet)

---

### Instagram Auto Following Bot :robot:
![Selenium](https://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=white)

[Portal :door:](https://github.com/Ken-Yeung/KensToolkit/tree/master/IgAutoFollow "Go to IgAutoFollow repo")

-   This is the very first script that I created 
-   Function included: aggressively generate numbers of Following and Follower for IG profile
-   Using Python plugin `selenium` to achieve the objective
-   It is able to follow 120 users per 10 hours (adjustable)
-   By that, it could generate 5-15 follower per day

### Usage:

-   Go to `info.txt`

1. Enter the value of Account
2. Enter the value of Password
3. Enter the value of TargetUser (Meaning: target user's profile name)
4. Then double click the `Start.exe` (Only for Windows)

-   For MacOs please run the code `python3 IGBOTv2.1.py`

<!-- ### :exclamation::exclamation::exclamation: Notice :exclamation::exclamation::exclamation: -->

#### :bangbang: Notice :bangbang:

-   Instagram seems to change their web layout regularly, therefore, please check the elements' XPATH is correct for current version of Instagram layout, if not, you should [modify](#modifying-xpath) before using it ( I did not update it for few months already )
-   Chrome remote driver might not work if the version of that does not match the version of Chrome in local
-   This script only works in CPU format of AMD
### Modifying XPATH

-   Please modify the values inside `IGBOTv2.1.py`

Variable | Value | Type
--- | --- | ---
ac_field | XPATH of account field | str
pw_field | XPATH of password field | str
login_btn | XPATH of login button | str
phone_verify_field | XPATH of Phone verify fields | str
verify_btn | XPATH of button of verify phone auth | str
later_save_info | XPATH of button in warning message of save later | str
home_icon | XPATH of Instagram's Icon | str
open_the_dialog | XPATH of the button that open the target followers dialog | str
dialog | XPATH of target followers dialog | str
follow_btn | XPATH of target followers button inside dialog | str

---

### Option Data Crawler :floppy_disk:

[Portal :door:](https://github.com/Ken-Yeung/KensToolkit/tree/master/OptionCrawler "Go to OptionCrawler repo")

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

---

### Link Tree :evergreen_tree:

[Portal :door:](https://github.com/Ken-Yeung/KensToolkit/tree/master/LinkDistributor "Go to LinkDistributor repo")

-   This is the [link tree](https://bit.ly/utaxihkapp "Go to uTaxi's Link Tree") I created for Company **uTaxi** as a gift
-   This is a server framework of `FastAPI`
-   It is capible to redirect user to google play store or app store base on user's preference
-   With the ability to track when and which link they clicked

<!-- ### :exclamation::exclamation::exclamation: Notice :exclamation::exclamation::exclamation: -->

#### :bangbang: Notice :bangbang:

-   This script might only works in CPU format of AMD

---

### File Transfer Server :card_index_dividers:

[Portal :door:](https://github.com/Ken-Yeung/KensToolkit/tree/master/FilesTransferrer_one_direction "Go to FilesTransferrer_one_direction repo")

-   This is a super simple [FTP](https://zh.wikipedia.org/zh-hk/%E6%96%87%E4%BB%B6%E4%BC%A0%E8%BE%93%E5%8D%8F%E8%AE%AE "What is FTP") that I created for convience use only
-   The reason for that is I found out there is difficulty to transfer files from mobile phones to computer, E.g. Transferring photos from iPhone to Windows OS
-   This script solved the problem by hosting a `FastAPI` server to recieve files via **same wifi enviornment**
-   Initially, transferred files would save inside database folder
-   Saving path could change by modifying the path in `.env`

### Usage

-   Then double click the `Upload.exe` (Only for Windows)

-   For MacOs please run the code `python3 main.py`

<!-- ### :exclamation::exclamation::exclamation: Notice :exclamation::exclamation::exclamation: -->

#### :bangbang: Notice :bangbang:

-   This script only works in CPU format of AMD

---

### Api Initial Template :file_cabinet:

[Portal :door:](https://github.com/Ken-Yeung/KensToolkit/tree/master/FastApiTemplate "Go to FastApiTemplate repo")

-   This is customized initial template for me to quickly start up a server for production

### Usage

-   Enter the command: `python3 main.py`

<!-- ### :exclamation::exclamation::exclamation: Notice :exclamation::exclamation::exclamation: -->

#### :bangbang: Notice :bangbang:

-   This script works in both CPU format of AMD and ARM
