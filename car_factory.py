from datetime import date
from car import Car
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery


class CarFactory:
    def create_calliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        calliope = Car()
        calliope.engine = CapuletEngine(last_service_mileage, current_mileage)
        calliope.battery = SpindlerBattery(last_service_date, current_date)
        return calliope
    
    def create_glissade(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int): 
        glissade = Car()
        glissade.engine = WilloughbyEngine(last_service_mileage, current_mileage)
        glissade.battery = SpindlerBattery(last_service_date, current_date)
        return glissade
    
    def create_palindrome(current_date: date, last_service_date: date, warning_light_on: bool): 
        palindrome = Car()
        palindrome.engine = SternmanEngine(warning_light_on)
        palindrome.battery = SpindlerBattery(last_service_date, current_date)
        return palindrome
    
    def create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int): 
        rorschach = Car()
        rorschach.engine = WilloughbyEngine(last_service_mileage, current_mileage)
        rorschach.battery = NubbinBattery(last_service_date, current_date)
        return rorschach
    
    def create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int): 
        thovex = Car()
        thovex.engine = CapuletEngine(last_service_mileage, current_mileage)
        thovex.battery = NubbinBattery(last_service_date, current_date)
        return thovex
    