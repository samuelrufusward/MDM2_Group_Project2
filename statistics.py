from demo import *
import re


def get_event_times_dict(all_events):

    events_list = []
    events_dict = {}
    vehicle_event_times_dict = {}

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
                vehicle_event_times_dict[vehicle] = {"arrives": arrival_time, "enters": enter_time, "exits": exit_time}

    return vehicle_event_times_dict


def get_average_wait_time_dict(vehicle_event_times_dict):

    all_wait_times = []
    small_car_wait_times = []
    large_vehicle_wait_times = []

    for vehicle in vehicle_event_times_dict:
        if "enters" not in vehicle_event_times_dict[vehicle] or "arrives" not in vehicle_event_times_dict[vehicle]:
            pass
        else:
            waiting_time = vehicle_event_times_dict[vehicle]["enters"] - vehicle_event_times_dict[vehicle]["arrives"]
            all_wait_times.append(waiting_time)

            if re.sub('[0-9]+', '', str(vehicle)) == "Small": # Checks if small vehicle
                small_car_wait_times.append(waiting_time)

            elif re.sub('[0-9]+', '', str(vehicle)) == "Large": # Checks if large vehicle
                large_vehicle_wait_times.append(waiting_time)

    average_wait_time = sum(all_wait_times) / len(all_wait_times) # Calculates wait time for all vehicles
    average_small_car_wait_time = sum(small_car_wait_times) / len(small_car_wait_times) # Wait time for small cars
    average_large_vehicle_wait_time = sum(large_vehicle_wait_times) / len(small_car_wait_times) # Large vehicles

    average_wait_time_dict = {"all": average_wait_time, "small": average_small_car_wait_time,
                              "large": average_large_vehicle_wait_time}

    return average_wait_time_dict

all_events = main()

events_dict = get_event_times_dict(all_events)

average_wait_times_dict = get_average_wait_time_dict(events_dict)

print(average_wait_times_dict)