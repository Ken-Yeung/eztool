import pathlib

def convert_path(data):
    raw_string = r"{}".format(data)
    p = pathlib.PureWindowsPath(rf'{repr(raw_string)[1:-1]}')
    p = p.as_posix()
    return p