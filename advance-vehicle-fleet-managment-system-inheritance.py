class Vehicle:
    def __init__(self, vehicle_id, make, model, year, daily_rate, is_available, mileage, fuel_type):
        self.vehicle_id = vehicle_id
        self.make = make
        self.model = model
        self.year = year
        self.daily_rate = daily_rate
        self.is_available = is_available
        self.mileage = mileage
        self.fuel_type = fuel_type

    def rent(self):
        if self.is_available:
            self.is_available = False
            return True
        else:
            return False
        
    def return_vehicle(self):
        if not self.is_available:
            self.is_available = True
            return True
        else:
            return False
        
    def calculate_rental_cost(self, days):
        return self.daily_rate * days
    
    def get_vehicle_info(self):
        return f"Vehicle ID: {self.vehicle_id}\nMake: {self.make}\nModel: {self.model}\nYear: {self.year}\nDaily Rate: {self.daily_rate}\nFuel Type: {self.fuel_type}\nMileage: {self.mileage}\nIs Available: {self.is_available}"
    
class Car(Vehicle):
    def __init__(self, vehicle_id, make, model, year, daily_rate, is_available, mileage, fuel_type, seating_capacity, transmission_type, has_gps):
        super().__init__(vehicle_id, make, model, year, daily_rate, is_available, mileage, fuel_type)
        self.seating_capacity = seating_capacity
        self.transmission_type = transmission_type
        self.has_gps = has_gps
        
    def calculate_rental_cost(self, days):
        return super().calculate_rental_cost(days) * 1.2

class Motorcycle(Vehicle):
    def __init__(self, vehicle_id, make, model, year, daily_rate, is_available, mileage, fuel_type, engine_cc, bike_type):
        super().__init__(vehicle_id, make, model, year, daily_rate, is_available, mileage, fuel_type)
        self.engine_cc = engine_cc
        self.bike_type = bike_type
        
    def calculate_rental_cost(self, days):
        return super().calculate_rental_cost(days) * 1.1
    
class Truck(Vehicle):
    def __init__(self, vehicle_id, make, model, year, daily_rate, is_available, mileage, fuel_type, cargo_capacity, license_required, max_weight):
        super().__init__(vehicle_id, make, model, year, daily_rate, is_available, mileage, fuel_type)
        self.cargo_capacity = cargo_capacity
        self.license_required = license_required
        self.max_weight = max_weight
        
    def calculate_rental_cost(self, days):
        return super().calculate_rental_cost(days) * 1.3

class MaintenanceRecord:
    def __init__(self, vehicle_id, maintenance_date, description, cost):
        self.vehicle_id = vehicle_id
        self.maintenance_date = maintenance_date
        self.description = description
        self.cost = cost
        
    def __str__(self):
        return f"Vehicle ID: {self.vehicle_id}\nMaintenance Date: {self.maintenance_date}\nDescription: {self.description}\nCost: {self.cost}"
    

