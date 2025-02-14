class Vehicle:
    def __init__(self, name, capacity, fare_per_person):
        self.name = name
        self.capacity = capacity
        self.fare_per_person = fare_per_person
    
    def total_fare(self):
        return self.capacity * self.fare_per_person

class Bus(Vehicle):
    def total_fare(self):
        base_fare = super().total_fare()
        maintenance_charge = base_fare * 0.1  # 10% additional maintenance charge
        return base_fare + maintenance_charge

# Example usage
bus = Bus("City Bus", 50, 20)
print(f"Total fare for {bus.name}: {bus.total_fare()} currency units")
