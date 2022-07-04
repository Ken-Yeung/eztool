import time

class timer:
    def __init__(self, debug=True) -> None:
        self.debug = debug
        self.head = "eztool [Timer]"

        self.startTime = 0
        self.endTime = 0
        return

    def start(self) -> str:
        self.startTime = time.perf_counter()

        if self.debug:
            print(f"{self.head}: Start timing.")

        return str(self.startTime)

    def stop(self) -> str:
        self.endTime = time.perf_counter()
        res = self.endTime - self.startTime

        if self.debug:
            print(f"{self.head}: Consumed {str(res)} seconds.")

        return str(res)