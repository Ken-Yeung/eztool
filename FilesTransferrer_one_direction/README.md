<h1 align="center">:card_index_dividers:<br>Welcome to File Transfer Server</h1>

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
2.  [Option Data Crawler](https://github.com/Ken-Yeung/KensToolkit/tree/master/OptionCrawler "Go to OptionCrawler repo")
3.  [Link Tree](https://github.com/Ken-Yeung/KensToolkit/tree/master/LinkDistributor "Go to LinkDistributor repo")
4.  [File Transfer Server](#file-transfer-server-card_index_dividers) <-- YOU ARE HERE
5.  [Api Initial Template](https://github.com/Ken-Yeung/KensToolkit/tree/master/FastApiTemplate "Go to FastApiTemplate repo")

-   [Back to Home Page](https://github.com/Ken-Yeung/KensToolkit "Home Page")

---

### File Transfer Server :card_index_dividers:

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