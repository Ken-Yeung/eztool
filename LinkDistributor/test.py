import og.og as og

def recorder(data:str):
    head = [
        ['datetime', 'platform']
    ]

    fmt = "%d-%m-%Y %H:%M"

    current_datetime = og.t_now(fmt).split(" ")
    month_year = "_".join(current_datetime[0].split("-")[1:])
    # print(month_year)
    worker = og.csv_worker(f"database/{month_year}.csv")
    # worker.write(detail)
    new_row = [" ".join(current_datetime), data]
    try:
        origin = worker.read()
        origin.append(new_row)
        worker.write(origin)
    except:
        head.append(new_row)
        worker.write(head)
    return

if __name__ == "__main__":
    # recorder("ios")
    og.glob_file()

    pass