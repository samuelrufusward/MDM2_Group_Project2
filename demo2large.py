##########################
#  actors.py
#
#  This file defines classes that make up the main actors in a simulation of a
#  bus picking up passengers from bus stops.
##########################

import random

from objects import Vehicle, TunnelSection, Tunnel

vehicles = []

tunnel_sections = [
    TunnelSection('East', (1711, 0), []),
    TunnelSection('West', (0, 0), []),
    TunnelSection('Middle', (800, 0), [])
]

model = Tunnel(tunnel_sections, vehicles, 2)

events = model.init()
quit1 = 0
while quit1 == 0:
    if events != []:
        print(events)
    events = model.update()



if __name__ == "__main__":
    import doctest
    doctest.testmod()

