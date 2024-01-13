class Bus:
    def __init__(self, bus_id, destination, departure_time, total_seats):
        self.bus_id = bus_id
        self.destination = destination
        self.departure_time = departure_time
        self.total_seats = total_seats
        self.available_seats = [i for i in range(1, total_seats + 1)]
        self.reservations = {}

    def display_schedule(self):
        print(f"Bus {self.bus_id} to {self.destination}, Departure Time: {self.departure_time}")
        print(f"Available Seats: {len(self.available_seats)}/{self.total_seats}")

    def reserve_seat(self, passenger, seat_number):
        if seat_number in self.available_seats:
            self.available_seats.remove(seat_number)
            self.reservations[seat_number] = passenger
            return True
        else:
            return False

    def cancel_reservation(self, seat_number):
        if seat_number in self.reservations:
            passenger = self.reservations[seat_number]
            self.available_seats.append(seat_number)
            del self.reservations[seat_number]
            return passenger
        else:
            return None


class BusCompany:
    def __init__(self, name):
        self.name = name
        self.buses = {}

    def add_bus(self, bus_id, destination, departure_time, total_seats):
        if bus_id not in self.buses:
            self.buses[bus_id] = Bus(bus_id, destination, departure_time, total_seats)
            print(f"Bus {bus_id} added to the schedule.")
        else:
            print(f"Bus {bus_id} already exists in the schedule.")

    def display_bus_schedule(self):
        print(f"{self.name} Bus Schedule:")
        for bus_id, bus in self.buses.items():
            bus.display_schedule()
            print()

    def update_bus_schedule(self, bus_id, destination=None, departure_time=None, total_seats=None):
        if bus_id in self.buses:
            bus = self.buses[bus_id]
            if destination:
                bus.destination = destination
            if departure_time:
                bus.departure_time = departure_time
            if total_seats:
                bus.total_seats = total_seats
                bus.available_seats = [i for i in range(1, total_seats + 1)]
            print(f"Bus {bus_id} schedule updated.")
        else:
            print(f"Bus {bus_id} does not exist in the schedule.")

# Example usage
bus_company = BusCompany("LüksSeyehatCompany")

# Add buses to the schedule
bus_company.add_bus("A123", "Mersin", "08:00", 20)
bus_company.add_bus("B456", "Ankara", "10:30", 30)

# Display bus schedule
bus_company.display_bus_schedule()

# Update bus schedule
bus_company.update_bus_schedule("A123", destination="Adana", departure_time="09:00", total_seats=25)

# Display updated bus schedule
bus_company.display_bus_schedule()
