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

    def reserve_seat(self, passenger_name, seat_number):
        if seat_number in self.available_seats:
            self.available_seats.remove(seat_number)
            self.reservations[seat_number] = passenger_name
            return True
        else:
            return False

class ReservationSystem:
    def __init__(self):
        self.buses = {}

    def add_bus(self, bus_id, destination, departure_time, total_seats):
        if bus_id not in self.buses:
            self.buses[bus_id] = Bus(bus_id, destination, departure_time, total_seats)
            print(f"Bus {bus_id} added to the schedule.")
        else:
            print(f"Bus {bus_id} already exists in the schedule.")

    def display_bus_schedule(self):
        print("Bus Schedule:")
        for bus_id, bus in self.buses.items():
            bus.display_schedule()
            print()

    def make_reservation(self, bus_id, passenger_name, seat_number):
        if bus_id in self.buses:
            bus = self.buses[bus_id]
            success = bus.reserve_seat(passenger_name, seat_number)
            if success:
                print(f"Reservation confirmed for {passenger_name} on Bus {bus_id}.")
                print(f"Seat Number: {seat_number}")
                return True
            else:
                print(f"Seat {seat_number} is not available on Bus {bus_id}.")
                return False
        else:
            print(f"Bus {bus_id} does not exist in the schedule.")
            return False

# Example usage
reservation_system = ReservationSystem()

# Add buses to the schedule
reservation_system.add_bus("A123", "Mersin", "08:00", 20)
reservation_system.add_bus("B456", "Ankara", "10:30", 30)

# Display bus schedule
reservation_system.display_bus_schedule()

# Make a reservation
reservation_system.make_reservation("A123", "Ali Kaya", 5)

# Display updated bus schedule
reservation_system.display_bus_schedule()