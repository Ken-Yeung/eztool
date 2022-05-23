import codecs

def html():
    html = codecs.open("./temp/main.html", "r").read()
    return html

def cdn(script):
    cdn = codecs.open(f"./cdn/{script}", "r").read()
    return cdn

if __name__ == "__main__":
    print("Start: ")
    # print(html())
    test_str = "name"
    spl = test_str.split(".")
    print(spl[-1])