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


class ReservationSystem:
    def __init__(self):
        self.buses = {}
        self.passengers = {}

    def add_passenger(self, username, full_name, email, phone):
        if username not in self.passengers:
            self.passengers[username] = Passenger(username, full_name, email, phone)
            print(f"Passenger {username} added to the system.")
        else:
            print(f"Passenger {username} already exists in the system.")

    def display_passenger_info(self, username):
        if username in self.passengers:
            self.passengers[username].display_info()
        else:
            print(f"Passenger {username} does not exist in the system.")

    def make_reservation(self, bus_id, username, seat_number):
        if bus_id in self.buses and username in self.passengers:
            bus = self.buses[bus_id]
            passenger = self.passengers[username]
            success = bus.reserve_seat(passenger, seat_number)
            if success:
                print(f"Reservation confirmed for {username} on Bus {bus_id}.")
                print(f"Seat Number: {seat_number}")
                return True
            else:
                print(f"Seat {seat_number} is not available on Bus {bus_id}.")
                return False
        else:
            print(f"Bus {bus_id} or Passenger {username} does not exist in the system.")
            return False

    def cancel_reservation(self, bus_id, seat_number):
        if bus_id in self.buses:
            bus = self.buses[bus_id]
            passenger = bus.cancel_reservation(seat_number)
            if passenger:
                print(f"Reservation canceled for {passenger.username} on Bus {bus_id}.")
                print(f"Seat Number: {seat_number}")
                return True
            else:
                print(f"Could not cancel reservation for Seat {seat_number} on Bus {bus_id}.")
                return False
        else:
            print(f"Bus {bus_id} does not exist in the system.")
            return False

    def update_passenger_info(self, username, new_full_name=None, new_email=None, new_phone=None):
        if username in self.passengers:
            passenger = self.passengers[username]
            if new_full_name:
                passenger.full_name = new_full_name
            if new_email:
                passenger.email = new_email
            if new_phone:
                passenger.phone = new_phone
            print(f"Passenger information updated for {username}.")
        else:
            print(f"Passenger {username} does not exist in the system.")

# Example usage
reservation_system = ReservationSystem()

# Add passenger
reservation_system.add_passenger("ali_kaya", "Ali Kaya", "ali@gmail.com", "123456789")

# Display passenger info
reservation_system.display_passenger_info("ali_kaya")

# Update passenger info
reservation_system.update_passenger_info("ali_kaya", new_email="ali_kaya@gmail.com")

# Display updated passenger info
reservation_system.display_passenger_info("ali_kaya")

# Add buses to the schedule
reservation_system.buses["A123"] = Bus("A123", "Mersin", "08:00", 20)

# Display bus schedule
reservation_system.buses["A123"].display_schedule()

# Make a reservation
reservation_system.make_reservation("A123", "ali_kaya", 5)

# Display updated bus schedule
reservation_system.buses["A123"].display_schedule()

# Cancel reservation
reservation_system.cancel_reservation("A123", 5)

# Display updated bus schedule
reservation_system.buses["A123"].display_schedule()