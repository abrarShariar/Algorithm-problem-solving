import DateTime
import datetime

class Locker:
    def __init__(self, timestamp, fee = 0):
        self.fee = fee
        self.timestamp = timestamp

    def get_locker_fee(self):
        if self.timestamp.is_weekday():
            if self.timestamp.time >= datetime.datetime.strptime('09:00:00', '%H:%M:%S') and self.timestamp.time < datetime.datetime.strptime('16:00:00', '%H:%M:%S'):
                return 500
            else:
                return 400
        else:
            if self.timestamp.time >= datetime.datetime.strptime('09:00:00', '%H:%M:%S') and self.timestamp.time < datetime.datetime.strptime('16:00:00', '%H:%M:%S'):
                return 700
            else:
                return 500
            