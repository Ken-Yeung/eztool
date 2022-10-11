<h1 align="center">:robot:<br>Welcome to Instagram Auto Following Bot</h1>

<div align="center">
<a herf="https://github.com/Ken-Yeung/KensToolkit.git"><img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="Python Badge"/></a>
<a herf="https://github.com/Ken-Yeung/KensToolkit.git"><img src="https://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=white" alt="Selenium Badge"/></a>
</div>

>   $ python --version
>
>   Python 3.7.0

### Here's my creation workflow :receipt:

1.  [Instagram Auto Following Bot](#instagram-auto-following-bot-robot) <-- YOU ARE HERE
2.  [Option Data Crawler](https://github.com/Ken-Yeung/KensToolkit/tree/master/OptionCrawler "Go to OptionCrawler repo")
3.  [Link Tree](https://github.com/Ken-Yeung/KensToolkit/tree/master/LinkDistributor "Go to LinkDistributor repo")
4.  [File Transfer Server](https://github.com/Ken-Yeung/KensToolkit/tree/master/FilesTransferrer_one_direction "Go to FilesTransferrer_one_direction repo")
5.  [Api Initial Template](https://github.com/Ken-Yeung/KensToolkit/tree/master/FastApiTemplate "Go to FastApiTemplate repo")

-   [Back to Home Page](https://github.com/Ken-Yeung/KensToolkit "Home Page")

---

### Instagram Auto Following Bot :robot:

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