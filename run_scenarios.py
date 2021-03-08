from statistics import get_event_times_dict, get_average_wait_time_dict
from objects import Vehicle, TunnelSection, Tunnel

vehicles = []

tunnel_sections = [
    TunnelSection('East', (1711, 0), [], []),
    TunnelSection('West', (0, 0), [], []),
    TunnelSection('Middle', (800, 0), [], [])
]


def run(model):
    all_events = []
    events = model.init()
    quit1 = 0

    while quit1 == 0:
        if events != []:
            #print(events)
            all_events.append(events)
        events = model.update()
        if events == "quit":

            return all_events


def run_all_scenarios():

    model0_wait_times = []

    for i in range(20):
        vehicles = []

        tunnel_sections = [
            TunnelSection('East', (1711, 0), [], []),
            TunnelSection('West', (0, 0), [], []),
            TunnelSection('Middle', (800, 0), [], [])
        ]

        model = Tunnel(tunnel_sections, vehicles, 2, 0, 0.08)

        events_list = run(model)

        events_dict = get_event_times_dict(events_list)

        average_wait_times_dict = get_average_wait_time_dict(events_dict)

        model0_wait_times.append(average_wait_times_dict)

    print(model0_wait_times)

    model1_wait_times = []

    for i in range(20):

        vehicles = []

        tunnel_sections = [
            TunnelSection('East', (1711, 0), [], []),
            TunnelSection('West', (0, 0), [], []),
            TunnelSection('Middle', (800, 0), [], [])
        ]

        model = Tunnel(tunnel_sections, vehicles, 2, 1, 0.08)

        events_list = run(model)

        events_dict = get_event_times_dict(events_list)

        average_wait_times_dict = get_average_wait_time_dict(events_dict)

        model1_wait_times.append(average_wait_times_dict)

    print(model1_wait_times)

    model2_wait_times = []

    for i in range(20):

        vehicles = []

        tunnel_sections = [
            TunnelSection('East', (1711, 0), [], []),
            TunnelSection('West', (0, 0), [], []),
            TunnelSection('Middle', (800, 0), [], [])
        ]

        model = Tunnel(tunnel_sections, vehicles, 2, 2, 0.08)

        events_list = run(model)

        events_dict = get_event_times_dict(events_list)

        average_wait_times_dict = get_average_wait_time_dict(events_dict)

        model2_wait_times.append(average_wait_times_dict)

    print(model2_wait_times)


    model3_wait_times = []

    for i in range(20):

        vehicles = []

        tunnel_sections = [
            TunnelSection('East', (1711, 0), [], []),
            TunnelSection('West', (0, 0), [], []),
            TunnelSection('Middle', (800, 0), [], [])
        ]

        model = Tunnel(tunnel_sections, vehicles, 2, 3, 0.08)

        events_list = run(model)

        events_dict = get_event_times_dict(events_list)

        average_wait_times_dict = get_average_wait_time_dict(events_dict)

        model3_wait_times.append(average_wait_times_dict)

    print(model3_wait_times)

    model4_wait_times = []

    for i in range(20):
        vehicles = []

        tunnel_sections = [
            TunnelSection('East', (1711, 0), [], []),
            TunnelSection('West', (0, 0), [], []),
            TunnelSection('Middle', (800, 0), [], [])
        ]

        model = Tunnel(tunnel_sections, vehicles, 2, 4, 0.08)

        events_list = run(model)

        events_dict = get_event_times_dict(events_list)

        average_wait_times_dict = get_average_wait_time_dict(events_dict)

        model4_wait_times.append(average_wait_times_dict)

    print(model4_wait_times)

    model5_wait_times = []

    for i in range(20):
        vehicles = []

        tunnel_sections = [
            TunnelSection('East', (1711, 0), [], []),
            TunnelSection('West', (0, 0), [], []),
            TunnelSection('Middle', (800, 0), [], [])
        ]

        model = Tunnel(tunnel_sections, vehicles, 2, 5, 0.08)

        events_list = run(model)

        events_dict = get_event_times_dict(events_list)

        average_wait_times_dict = get_average_wait_time_dict(events_dict)

        model5_wait_times.append(average_wait_times_dict)

    print(model5_wait_times)

    return [model0_wait_times, model1_wait_times, model2_wait_times, model3_wait_times, model4_wait_times,
            model5_wait_times]