import datetime

class DateTime:
    def __init__(self, timestamp):
        self.timestamp = timestamp
        self.valid_format = '%Y-%m-%d %H:%M:%S'
        self.business_start_time = datetime.datetime.strptime('09:00:00', '%H:%M:%S')
        self.business_end_time = datetime.datetime.strptime('21:00:00', '%H:%M:%S')

        self.day_dict = {
            0: 'Monday',
            1: 'Tuesday',
            2: 'Wednesday',
            3: 'Thursday',
            4: 'Friday',
            5: 'Saturday',
            6: 'Sunday'
        }

        # split the date and time and set separately
        date_time_list = self.timestamp.split(' ')
        self.date = datetime.datetime.strptime(date_time_list[0], '%Y-%m-%d')
        self.time = datetime.datetime.strptime(date_time_list[1], '%H:%M:%S')

        # set the day
        self.day = datetime.datetime.strptime(date_time_list[0], '%Y-%m-%d')
        self.day = self.day.weekday()
        
    def is_format_valid(self):
        try:
            datetime.datetime.strptime(self.timestamp, self.valid_format)
        except:
            return False
        return True

    def is_valid_business_hours(self):
        if self.time >= self.business_start_time and self.time <= self.business_end_time:
            return True
        else:
            return False

    def is_weekday(self):
        if self.day >= 0 and self.day <= 4:
            return True
        return False

    

