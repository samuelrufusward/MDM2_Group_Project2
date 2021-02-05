import matplotlib.pyplot as plt
import sys
from matplotlib.animation import FuncAnimation

from busstop.objects import Bus, BusStop, BusPassenger
from busstop.linear import LinearBusRouteModel
from busstop.analytical_tools import *


def animate_model(model):
    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1])

    time = -1  # time
    events = model.init()
    for event in events:
        print((time,) + event)

    def init():
        # Initialise the graphics
        return model.init_animation(ax)

    def update(frame_number):
        # Update the simulation
        time = frame_number
        events = model.update()
        for event in events:
            frame_number += 1
            timed_event = (time,) + event
            print(timed_event)
            # Sends events with frame number to analytical tools
            #all_events = get_event(timed_event)
            #if time > 10000000:
            #    analyse_events(all_events)
            #    sys.exit()
        # Update the graphics
        return model.update_animation()

    animation = FuncAnimation(fig, update, init_func=init, blit=True)
    plt.plot([50, 50], [-50, 50], 'k-', linewidth=3)
    plt.show()
