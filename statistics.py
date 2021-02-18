from demo import *

all_events = main()

events_list = []
events_dict = {}
vehicle_event_times = {}

for sublist in all_events:
    if sublist is not None:
        for element in sublist:
            if element is not None:
                events_list.append(element)

for event in events_list:
    vehicle = event[1]
    if vehicle not in events_dict:
        events_dict[vehicle] = []

    events_dict[vehicle].append(event)

for vehicle in events_dict:

    vehicle_events = events_dict[vehicle]

    if len(vehicle_events) < 3:
        pass
    else:
        arrival_time = None
        enter_time = None
        exit_time = None
        for event in vehicle_events:
            if event[0] == "arrives":
                arrival_time = event[3]
            elif event[0] == "enters":
                enter_time = event[3]
            elif event[0] == "exits":
                exit_time = event[3]
        if arrival_time is None or enter_time is None or exit_time is None:
            pass
        else:
            vehicle_event_times[vehicle] = {"arrives": arrival_time, "enters": enter_time, "exits": exit_time}

print(vehicle_event_times)

average_queue_time = sum([vehicle_event_times[vehicle]["enters"] - vehicle_event_times[vehicle]["arrives"]
                          for vehicle in vehicle_event_times]) / len(vehicle_event_times)
print("average queue time:", average_queue_time)