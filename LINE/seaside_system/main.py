import sys
from DateTime import DateTime
from Shower import Shower
from Locker import Locker

locker_count = 0
user_locker_dict = {}
user_shower_dict = {}
user_shower_date_dict = {}

def main(line):
    global locker_count
    global user_locker_dict
    global user_shower_dict
    global user_shower_date_dict

    line = line.split(' ')
    use_type = line[0]
    input_timestamp = line[1] + ' ' + line[2]
    user_id = line[3]

    if use_type == 'shower:':
        user_age = line[4]
    elif use_type == 'locker:':
        desired_number_of_locker = int(line[4])
    elif use_type == 'lock:':
        locked_lockers = int(line[4])

    timestamp = DateTime(input_timestamp)
    
    # for shower usage
    if use_type == 'shower:':
        shower = Shower(user_age)
        if not timestamp.is_valid_business_hours():
            print("{} closed".format(use_type))
        elif user_id in user_shower_dict.keys() or (user_id in user_shower_date_dict.keys() and user_shower_date_dict[user_id] == timestamp):
            print("{} already accepted".format(use_type))
        else:
            user_shower_dict[user_id] = user_shower_dict.get(user_id, 0) + 1
            user_shower_date_dict[user_id] = timestamp
            print("{} {} {}".format(use_type, user_id, shower.get_shower_fee()))

    # for locker usage
    elif use_type == 'locker:':
        locker = Locker(timestamp)
        if not timestamp.is_valid_business_hours():
            print("{} closed".format(use_type))
        elif desired_number_of_locker > locker_count:
            print("locker: invalid number")
        else:
            locker_count -= 1
            user_locker_dict[user_id] = user_locker_dict.get(user_id, 0) + 1
            print("{} {} {} {}".format(use_type, user_id, locker.get_locker_fee(), locker_count))
    
    # for locker locking query
    elif use_type == 'lock:':
        if not timestamp.is_valid_business_hours():
            print("{} closed".format(use_type))
        elif user_locker_dict.get(user_id, 0) < locked_lockers:
            print('lock: invalid number')
        else:
            print('lock: accepted')

if __name__ == '__main__':
    input_count = 0
    for line in sys.stdin:
        if input_count == 0:
            locker_count = int(line)
            input_count += 1
        else:
            main(line)

