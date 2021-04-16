#!/usr/bin/env python3

import re
import csv

from collections import OrderedDict

# dictionary to keep track of the error type
per_user = {

}

error = {
    "Timeout while retrieving information": 0,
    "The ticket was modified while updating": 0,
    "Connection to DB failed": 0,
    "Tried to add information to a closed ticket": 0,
    "Permission denied while closing ticket": 0,
    "Ticket doesn't exist": 0
}
# iterate over all entries in the log file
with open('syslog.log') as file:
    for line in file:
        # check if its a error msg
        line = line.strip()
        name = re.findall(r'[(][a-zA-z.]*[)]', line)[0]
        name = name[1:len(name)-1]

        if name not in per_user.keys():
            per_user[name] = {"ERROR": 0, "INFO": 0}

        # if its an ERROR
        if(re.search(r"ERROR",line)):
            for error_key in error.keys():
                if (re.search(error_key, line)):
                    error[error_key] = error.get(error_key, 0) + 1
                    per_user[name]["ERROR"] = per_user[name]["ERROR"] + 1 
                    break
        
        # if its an INFO
        elif (re.search(r"INFO", line)):
            per_user[name]["INFO"] = per_user[name]["INFO"] + 1 

    error = sorted(error.items(), key = lambda x: x[1], reverse = True)
    error.insert(0, ("Error", "Count"))

    per_user = sorted(per_user.items(), key = lambda x: x[0])
    per_user.insert(0, ("Username", "INFO", "ERROR"))

file.close()
# store error to csv file
with open("error_message.csv", "w") as error_csv_file:
    writer = csv.writer(error_csv_file)
    for e in error:
        writer.writerow([e[0], e[1]])

error_csv_file.close()

# store per user to csv file
with open("user_statistics.csv", "w") as user_statistics_file:
    writer = csv.writer(user_statistics_file)
    writer.writerow([per_user[0][0], per_user[0][1], per_user[0][2]])
    for user_data in per_user[1:]:
        writer.writerow([user_data[0], user_data[1]['INFO'], user_data[1]['ERROR']])

user_statistics_file.close()
