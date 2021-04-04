# sort events by date
def get_event_date(event):
    return event.date 

def current_users(events):
    events.sort(key=get_event_date)
    machines = {}
    for event in events:
        machine = events['machine']
        if machine not in machines:
            machines[machine] = set()

        if event.type == "login":
            machines[machine].add(event['user'])
        elif event.type == "logout":
            if event['user'] in machines[machine]:
                machines[machine].remove(event['user'])

    return machines

def generate_report(machines):
    for machine_key, machine_data in machines.items():
        if len(machine_data) > 0:
            user_data = ", ".join(machine_data)
            print("{}: {}".format(machine_key, user_data))

# store dictioanry of sets
# prints the dictionary