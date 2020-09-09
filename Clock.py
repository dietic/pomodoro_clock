class Clock:
    def __init__(self, t, l="m"):
        self.t = t
        self.l = l

    def get_time_in_seconds(self):
        switcher = {
            "s": self.t,
            "h": self.t*60*60,
            "m": self.t*60
        }
        return switcher.get(self.l, "error")


clock = Clock(2231, "h")

print(clock.get_time_in_seconds())
