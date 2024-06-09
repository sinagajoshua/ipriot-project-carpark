from sensor import Sensor
from display import Display
class CarPark:
    def __init__(self,
                 location,
                 capacity,
                 log_file = 'log.txt',
                 plates = None,
                 sensors = None,
                 displays = None):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.sensors = sensors or []
        self.displays = displays or []


    def available_bays(self):
        return max(0, self.capacity - len(self.plates))

    def __str__(self):
        return f"Welcome to {self.location} car park"

    def register(self, component):
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Invalid component type!")

        if isinstance(component, Sensor):
            self.sensors.append(component)
        elif isinstance(component, Display):
            self.displays.append(component)
        # Below is commented because the top one is better
        '''else:
            raise TypeError("Invalid component type!")'''

    def add_car(self, plate):
        self.plates.append(plate)
        self._log_car("entered", plate)

    def remove_car(self, plate):
        self.plates.remove(plate)
        self._log_car("exited", plate)

    def update_displays(self):
        for display in self.displays:
            display.update({"Bays": self.available_bays(),
                            "Temperature": 42,
                            "News": "Nice things happened today"}
                           )
            print(f"Updating: {display}")