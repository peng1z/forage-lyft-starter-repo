from abc import abstractmethod


class Tire(ABC):
    @abstractmethod
    def needs_service(self):
        pass