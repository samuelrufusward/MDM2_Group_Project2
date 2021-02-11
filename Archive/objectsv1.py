##########################
#  actors.py
#
#  This file defines classes that make up the main actors in a simulation of a
#  bus picking up passengers from bus stops.
##########################

import random

class Printable:
    """Mixin to add printing functionality to subclasses.

    Examples
    ========

    A subclass just needs to define parameters and will print nicely::

        >>> class Thing(Printable):
        ...     parameters = 'foo', 'bar'
        ...     def __init__(self, foo, bar):
        ...         self.foo = foo
        ...         self.bar = bar
        >>> t = Thing(3, 'qwe')
        >>> t
        Thing(3, 'qwe')
    """
    def __repr__(self):
        classname = type(self).__name__
        args = [getattr(self, p) for p in self.parameters]
        return '%s(%s)' % (classname, ', '.join(map(repr, args)))


class Vehicle(Printable):
    """Vehicle travelling through tunnel

    Parameters
    ==========

    name: str, the name of the vehicle
    source: str, the name of the starting tunnel end
    destination: str, the name of the ending tunnel end
    position: tuple(int,int), position of the vehicle
    direction: int, 1 if moving right and -1 if moving left
    speed: int, conrols the speed of the bus

    Examples
    ========

    Create a vehicle:

        >>> random10 = Vehicle('random10', 'East', 'West', (20, 0), 1, 1)
        >>> random10
        Vehicle('random10', 'East', 'West', (20, 0), 1, 1)
    

    All attributes are public:

        >>> random10.name
        'random10'
    """
    parameters = 'name', 'source', 'destination', 'section', 'position', 'direction', 'speed', 'size'

    def __init__(self, name, source, destination, arrival_time, position, direction, speed, size):

        if not isinstance(name, str):
            raise TypeError('name should be a string')
        if not isinstance(source, str):
            raise TypeError('source should be a string')
        if not isinstance(destination, str):
            raise TypeError('destination should be a string')
        if not (isinstance(position, tuple) and len(position) == 2 and
                all(isinstance(c, int) for c in position)):
            raise TypeError('position should be a pair of ints')
        if direction not in {1, -1}:
            raise TypeError('direction should be 1 or -1')
        if not isinstance(speed, int):
            raise TypeError('speed should be int')
        if int(speed) < 0:
            raise TypeError('speed must be positive')
        self.name = name
        self.source = source
        self.destination = destination
        self.arrival_time = arrival_time
        self.position = position
        self.direction = direction
        self.speed = speed
        self.size = size


class TunnelSection(Printable):
    """Tunnel end with waiting vehicles

    Parameters
    ==========

    name: str, describes which end of the tunnel it is
    position: tuple(int,int), coordinates of the tunnel end
    vehicles: list[vehicles], list of the vehicles waiting at the stop

    Examples
    ========

    Create a vehicle and add to the tunnel end:

        >>> random10 = Vehicle('random10', 'East', 'West', (20, 0), 1, 1)
        >>> tunnelend = TunnelEnd('East', (20, 0), [random10])
        >>> tunnelend
        TunnelEnd('East', (20, 0), [Vehicle('random10', 'East', 'West', (20, 0), 1, 1)])

    """
    parameters = 'name', 'position', 'vehicles'

    def __init__(self, name, position, vehicles):

        if not isinstance(name, str):
            raise TypeError('name should be a string')
        if not (isinstance(position, tuple) and len(position) == 2 and
                all(isinstance(c, int) for c in position)):
            raise TypeError('position should be a pair of ints')
        if not all(isinstance(v, Vehicle) for v in vehicles):
            raise TypeError('vehicles should be a list of Vehicles')
        if not all(v.source == name for v in vehicles):
            raise ValueError('vehicle at the wrong end')

        self.name = name
        self.position = position
        self.vehicles = list(vehicles)


class Tunnel(Printable):
    """Tunnel with vehicles

    Parameters
    ==========

    east_end: int, coordinate of east end of the tunnel
    west_end: int, coordinate of west end of the tunnel
    ends: list[TunnelEnd], list of tunnel ends
    vehicles: list[Vehicles], list of the vehicles in the tunnel
    rates: dict[str,float] (optional) rates of vehicles arriving


    Examples
    ========

    First create passengers, buses and bus stops:

        >>> random10 = Vehicle('random10', 'East', 'West', (20, 0), 1, 1)
        >>> random11 = Vehicle('random11', 'West', 'East', (40, 0), 1, 1)
        >>> tunnelends = [TunnelEnd('East', (20, 0), [random10]),
        ...             TunnelEnd('West', (20, 0), [random11])]

    Finally we are ready to create a complete tunnel model with 2 end and
    2 vehicles:

        >>> model = Tunnel(-50, 50, tunnelends, [random10, random11])

    """

    def __init__(self, sections, vehicles, way):
        self.sections = list(sections)
        self.vehicles = list(vehicles)
        self.way = way

    def init(self):
        self.time = 8
        self.vehicle_num = 0

        events = []
        for section in self.sections:
            if section.name != 'Middle':
                for vehicle in section.vehicles:
                    events.append(('arrives', vehicle.name, end.name))

        return events

    def update(self):
        self.time += (1/60)

        if self.time >= 20:
            quit()
        
        events = []

        for section in self.sections:
            if section.name == 'Middle':
                events += self.update_middle(section)
            else:
                events += self.update_end(section)

        return events

    def update_middle(self, middle):
        """Update simulation state of vehicle."""

        events = []
        
        for vehicle in middle.vehicles:
            # Using speed input from vehicle class to accomidate different speeds
            old_x, old_y = vehicle.position
            new_x = old_x + vehicle.speed * vehicle.direction
            new_y = old_y  # vehicle moves horizontally
            vehicle.position = (new_x, new_y)
    
            events = []

            # Does the vehicle reach the its destination
            for section in self.sections:
                if section.name == vehicle.destination:
                    end_x, end_y = section.position
                    if old_x < end_x <= new_x or new_x < end_x <= old_x:
                        middle.vehicles.remove(vehicle)
                        self.vehicles.remove(vehicle)
                        events.append(('exits', vehicle.name, vehicle.destination, self.time-vehicle.arrival_time))
                            

        return events

        

    def update_end(self, end):
        """Update tunnel end"""

        events = []
        
        # New vehicles arrive randomly at each end of the tunnel. The probability of
        # a vehicle arriving is given by 1 - self.rates[self.name].
        if 0.1 > random.random():
            # A new vehicle randomly arrives. They want to go
            # to the other end of the tunnel
            name = 'random' + str(self.vehicle_num)
            self.vehicle_num += 1
            
            for tunnel_section in self.sections:
                if (tunnel_section.name != 'Middle') and (tunnel_section != end):
                    destination = tunnel_section

            x_source, y_source = end.position
            x_destination, y_destination = destination.position
            direction = (x_destination-x_source)/abs(x_destination-x_source)
                    
            vehicle = Vehicle(name, end.name, destination.name, self.time, end.position, direction, 600, 'Small')
            self.vehicles.append(vehicle)
            events.append(('arrives', vehicle.name, end.name))

            if self.way == 2:
                self.sections[2].vehicles.append(vehicle)
                events.append(('enters', vehicle.name, end.name))
            elif self.way == 1:
                end.vehicles.append(vehicle)
            
        return events


if __name__ == "__main__":
    import doctest
    doctest.testmod()

