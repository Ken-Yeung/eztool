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

### Here's my creation workflow :receipt:

1.  [Instagram Auto Following Bot](#instagram-auto-following-bot-robot)
2.  [Option Data Crawler](#option-data-crawler-floppy_disk)
3.  [Link Tree](#link-tree-evergreen_tree)
4.  [File Transfer Server](#file-transfer-server-card_index_dividers)
5.  [Api Initial Template](#api-initial-template-file_cabinet)

---

### Instagram Auto Following Bot :robot:

[Portal :door:](https://github.com/Ken-Yeung/KensToolkit/tree/master/IgAutoFollow "Go to IgAutoFollow repo")

-   This is the very first script that I created for aggressively generate numbers of Following and Follower for IG profile
-   Using Python plugin `selenium` to achieve the objective
-   It is able to follow 120 users per 10 hours (adjustable)
-   By that, it could generate 10-15 follower per day

### Usage:

-   Go to `info.txt`

1. Enter the value of Account
2. Enter the value of Password
3. Enter the value of TargetUser (Meaning: target user's profile name)
4. Then double click the `Start.exe` (Only for Windows)

-   For MacOs please run the code `python3 IGBOTv2.1.py`

### :exclamation::exclamation::exclamation: Notice :exclamation::exclamation::exclamation:

-   Instagram would change their web layout regularly, therefore, please check and [modify](#modifying-xpath) the elements' XPATH is correct for current version of Instagram layout before using it ( I did not update it for few months already )
-   Chrome remote driver might not work if the version of that does not match the version of Chrome in local

### Modifying XPATH

-   Please modify the values inside `IGBOTv2.1.py`

```
ac_field = 'XPATH of account field'
pw_field = 'XPATH of password field'
login_btn = 'XPATH of login button'

phone_verify_field = 'XPATH of Phone verify fields'
verify_btn = 'XPATH of button of verify phone auth'

later_save_info = 'XPATH of button in warning message of save later'

home_icon = 'XPATH of Instagram's Icon'

open_the_dialog = 'XPATH of the button that open the target followers dialog'
dialog = 'XPATH of target followers dialog'
follow_btn = 'XPATH of target followers button inside dialog'
```

---

### Option Data Crawler :floppy_disk:

[Portal :door:](https://github.com/Ken-Yeung/KensToolkit/tree/master/OptionCrawler "Go to OptionCrawler repo")

-   This script is crawling Hong Kong options' data using plugins `selenium` and `pandas_datareader`
-   Extracting 3 options' data of call and put bid price, strike price where strike price is closest to current stock price.
-   To extract specific company's stock, option data, you have to change the Row values of companies code in `stock_list.xlsx` sheet of `data`

1. Stock price would display in sheet: `data`
2. Option data would display in sheet: `strike`

### Usage:

-   Enter the command: `python3 main.py`

### :exclamation::exclamation::exclamation: Notice :exclamation::exclamation::exclamation:

-   Chrome remote driver might not work if the version of that does not match the version of Chrome in local

---

### Link Tree :evergreen_tree:

[Portal :door:](https://github.com/Ken-Yeung/KensToolkit/tree/master/LinkDistributor "Go to LinkDistributor repo")

-   Description

---

### File Transfer Server :card_index_dividers:

[Portal :door:](https://github.com/Ken-Yeung/KensToolkit/tree/master/FilesTransferrer_one_direction "Go to FilesTransferrer_one_direction repo")

-   Description

---

### Api Initial Template :file_cabinet:

[Portal :door:](https://github.com/Ken-Yeung/KensToolkit/tree/master/FastApiTemplate "Go to FastApiTemplate repo")

-   Description
