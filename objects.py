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

    def __init__(self, name, source, destination, arrival_time, position, direction, size):

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
        self.name = name
        self.source = source # End of the tunnel the vehicle arrives at
        self.destination = destination # End of the tunnel the vehicle exits from
        self.arrival_time = arrival_time
        self.position = position # Current position of vehicle
        self.direction = direction
        self.size = size # Large or Small


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
        self.vehicles = list(vehicles) # List of vehicles in this tunnel section
        # i.e. waiting at tunnel end or in the tunnel


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
        self.sections = list(sections) # West/East ends and the Middle of the tunnel
        self.vehicles = list(vehicles) # This includes waiting vehicles and vehicles within the tunnel
        self.way = way # 2-way, 1-way or 0 traffic flow
        # 1-way traffic flow has 4 different options:
        # 10 - Traffic flowing from West to East is allowed to enter, there is no large vehicle
        # 11 - Traffic flowing from East to West is allowed to enter, there is no large vehicle
        # 12 - Traffic flowing from West to East is allowed to enter, there is a large vehicle
        # 13 - Traffic flowing from East to West is allowed to enter, there is a large vehicle
        

    def init(self):
        # The simulation begins at 8:00am, when the stations open
        self.time = 8
        self.vehicle_num = 0
        self.speed = 10 # Speed in metres/second
        self.large = '' # Specifies which end has a large vehicle 

    def update(self):
        # Each update equates to 1 second passing
        self.time += (1/3600)

        # The simulation finishes at 8:00pm, when the stations close
        if self.time >= 20:
            quit()
        
        events = []
        if self.way == 2:
            self.speed = 9.6
            for section in self.sections:
                if section.name == 'Middle':
                    events += self.update_middle(section)
                else:
                    events += self.update_arrivals(section)
                    if self.way == 2:
                        events += self.update_entries(section)
        elif self.way == 10:
            self.speed = 9.6
            for section in self.sections:
                if section.name == 'Middle':
                    events += self.update_middle(section)
                else:
                    events += self.update_arrivals(section)
                    if section.name == 'West':
                        events += self.update_entries(section)
                        
        elif self.way == 11:
            self.speed = 9.6
            for section in self.sections:
                if section.name == 'Middle':
                    events += self.update_middle(section)
                else:
                    events += self.update_arrivals(section)
                    if section.name == 'East':
                        events += self.update_entries(section)
                        
        elif self.way == 12:
            self.speed = 7.6
            for section in self.sections:
                if section.name == 'Middle':
                    events += self.update_middle(section)
                else:
                    events += self.update_arrivals(section)
                    if section.name == 'West':
                        events += self.update_entries(section)
                        
        elif self.way == 13:
            self.speed = 7.6
            for section in self.sections:
                if section.name == 'Middle':
                    events += self.update_middle(section)
                else:
                    events += self.update_arrivals(section)
                    if section.name == 'East':
                        events += self.update_entries(section)
                        
        elif self.way == 0:
            if self.large == 'West':
                if all(v.direction == 1 for v in self.sections[2].vehicles):
                    # If all vehicles in the tunnel are travelling from West to East
                    # we will wait for 1 minute before releasing the large vehicle
                    for i in range(60):
                        self.time += (1/3600)
                        for section in self.sections:
                            if section.name == 'Middle':
                                events += self.update_middle(section)
                            else:
                                events += self.update_arrivals(section)
                    self.way = 12
                    if all(v.size == 'Small' for v in self.sections[0].vehicles):
                        self.large = ''
                    else:
                        self.large = 'East'
                else:
                    # If there are vehicles travelling from East to West we must
                    # wait until these vehicles exit
                    for section in self.sections:
                        if section.name == 'Middle':
                            events += self.update_middle(section)
                        else:
                            events += self.update_arrivals(section)
                            
            else:
                if all(v.direction == -1 for v in self.sections[2].vehicles):
                    # If all vehicles in the tunnel are travelling from East to West
                    # we will wait for 1 minute before releasing the large vehicle
                    for i in range(60):
                        self.time += (1/3600)
                        for section in self.sections:
                            if section.name == 'Middle':
                                events += self.update_middle(section)
                            else:
                                events += self.update_arrivals(section)
                    self.way = 13
                    if all(v.size == 'Small' for v in self.sections[1].vehicles):
                        self.large = ''
                    else:
                        self.large = 'West'
                else:
                    # If there are vehicles travelling from West to East we must
                    # wait until these vehicles exit
                    for section in self.sections:
                        if section.name == 'Middle':
                            events += self.update_middle(section)
                        else:
                            events += self.update_arrivals(section)
                        
            
        return events

    def update_middle(self, middle):
        """Update simulation state of vehicle."""
        
        events = []
        
        for vehicle in middle.vehicles:
            # Using speed input from vehicle class to accomidate different speeds
            old_x, old_y = vehicle.position
            new_x = old_x + self.speed * vehicle.direction
            new_y = old_y  # vehicle moves horizontally
            vehicle.position = (new_x, new_y)
    
            events = []

            # Does the vehicle reach the its destination?
            for section in self.sections:
                if section.name == vehicle.destination:
                    end_x, end_y = section.position
                    if old_x < end_x <= new_x or new_x < end_x <= old_x:
                        middle.vehicles.remove(vehicle)
                        self.vehicles.remove(vehicle)
                        events.append(('exits', vehicle.name, vehicle.destination, self.time-vehicle.arrival_time))
                        if vehicle.size == 'Large' and all(v.size == 'Small' for v in middle.vehicles):
                            # If the exiting vehicle is large and all the remaining
                            # vehicles in the tunnel are small
                            if self.large == '':
                                # Go back to 2-way traffic if there are no more large vehicles
                                self.way = 2
                            else:
                                # Go back to 0 traffic flow if a large vehicle is waiting
                                self.way = 0
                            

        return events

        

    def update_arrivals(self, end):
        """Update vehicles that have arrived"""

        events = []
        
        # New vehicles arrive randomly at each end of the tunnel. The probability of
        # a vehicle arriving within a given second is given by 1 - rate.
        rate = 0.002
        proportion_large = 0.2
        # This is the proportion of vehicles we expect to be 'Large' which will require 1 way traffic flow
        if rate > random.random():
            # A new vehicle randomly arrives. They want to go to the other end of the tunnel
            if proportion_large > random.random():
                size = 'Large'
                if self.large == '':
                    self.large = end.name
                if self.way == 2:
                    self.way = 0
            else:
                size = 'Small'
                    
            name = size + str(self.vehicle_num)
            self.vehicle_num += 1
            
            for tunnel_section in self.sections:
                if (tunnel_section.name != 'Middle') and (tunnel_section != end):
                    destination = tunnel_section

            x_source, y_source = end.position
            x_destination, y_destination = destination.position
            direction = (x_destination-x_source)/abs(x_destination-x_source)

            vehicle = Vehicle(name, end.name, destination.name, self.time, end.position, direction, size)
            self.vehicles.append(vehicle)
            events.append(('arrives', vehicle.name, end.name, self.time))
            end.vehicles.append(vehicle)

        return events

    def update_entries(self, end):
        """Update vehicle that have entered the tunnel"""

        events = []

        for vehicle in end.vehicles:
            self.sections[2].vehicles.append(vehicle)
            events.append(('enters', vehicle.name, end.name, self.time-vehicle.arrival_time))
        end.vehicles.clear()
                
            
        return events


if __name__ == "__main__":
    import doctest
    doctest.testmod()

