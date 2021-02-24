
from statistics import get_event_times_dict, get_average_wait_time_dict
from objects import Vehicle, TunnelSection, Tunnel

vehicles = []

tunnel_sections = [
    TunnelSection('East', (1711, 0), [], []),
    TunnelSection('West', (0, 0), [], []),
    TunnelSection('Middle', (800, 0), [], [])
]


model1 = Tunnel(tunnel_sections, vehicles, 2, 0)
model2 = Tunnel(tunnel_sections, vehicles, 2, 1)


models = [model1, model2]


def run(model):
    all_events = []
    events = model.init()
    quit1 = 0

    while quit1 == 0:
        if events != []:
            print(events)
            all_events.append(events)
        events = model.update()
        if events == "quit":

            return all_events


for model in models:
    all_events = run(model)

    events_dict = get_event_times_dict(all_events)

    average_wait_times_dict = get_average_wait_time_dict(events_dict)

    print(average_wait_times_dict)
