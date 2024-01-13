class Passenger:
    def __init__(self, username, full_name, email, phone):
        self.username = username
        self.full_name = full_name
        self.email = email
        self.phone = phone

    def display_info(self):
        print(f"Username: {self.username}")
        print(f"Full Name: {self.full_name}")
        print(f"Email: {self.email}")
        print(f"Phone: {self.phone}")


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

    def get_income(self):
        # Calculate total income for the bus
        return len(self.reservations) * 50  # Assuming a fixed ticket price of $50


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

    def view_income_reports(self):
        total_income = 0
        print(f"Income Reports for {self.name}:")
        for bus_id, bus in self.buses.items():
            income = bus.get_income()
            total_income += income
            print(f"Bus {bus_id} - Total Income: ${income}")
        print(f"Total Income for {self.name}: ${total_income}")


# Example usage
bus_company = BusCompany("LüksSeyehatCompany")

# Add buses to the schedule
bus_company.add_bus("A123", "Mersin", "08:00", 20)
bus_company.add_bus("B456", "Ankara", "10:30", 30)

# Display bus schedule
bus_company.display_bus_schedule()

# Make a reservation
bus_company.buses["A123"].reserve_seat(Passenger("ali_kaya", "Ali Kaya", "ali@gmail.com", "123456789"), 5)

# View income reports
bus_company.view_income_reports()