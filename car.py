from abc import ABC
from engine.engine import Engine
from battery.battery import Battery
from serviceable import serviceable


class Car(serviceable, ABC):
    def __init__(self):
        self.engine = Engine()
        self.battery = Battery()

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service()
