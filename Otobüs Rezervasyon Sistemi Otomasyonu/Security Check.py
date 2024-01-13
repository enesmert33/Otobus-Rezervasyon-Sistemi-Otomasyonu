import hashlib
import random

class Passenger:
    def __init__(self, username, full_name, email, phone):
        self.username = username
        self.full_name = full_name
        self.email = email
        self.phone = phone
        self.password = self._hash_password("default_password")  # Hash the default password

    def _hash_password(self, password):
        # Simulate password hashing using hashlib (in a real system, use a secure hashing algorithm)
        return hashlib.sha256(password.encode()).hexdigest()

    def verify_password(self, password):
        # Verify the entered password with the stored hashed password
        return self.password == self._hash_password(password)

    def display_info(self):
        print(f"Username: {self.username}")
        print(f"Full Name: {self.full_name}")
        print(f"Email: {self.email}")
        print(f"Phone: {self.phone}")


class PaymentSystem:
    @staticmethod
    def process_payment(passenger, amount):
        # Simulate payment processing securely
        transaction_id = random.randint(100000, 999999)
        print(f"Processing payment of {amount} for {passenger.full_name}... Payment successful! Transaction ID: {transaction_id}")
        return transaction_id


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

    def authenticate_passenger(self, username, password):
        if username in self.passengers:
            passenger = self.passengers[username]
            if passenger.verify_password(password):
                print(f"Passenger {username} authenticated successfully.")
                return True
            else:
                print(f"Invalid password for passenger {username}.")
                return False
        else:
            print(f"Passenger {username} does not exist in the system.")
            return False

    def make_reservation(self, bus_id, username, seat_number, amount):
        if bus_id in self.buses and username in self.passengers:
            bus = self.buses[bus_id]
            passenger = self.passengers[username]
            success = bus.reserve_seat(passenger, seat_number)
            if success:
                print(f"Reservation confirmed for {username} on Bus {bus_id}.")
                print(f"Seat Number: {seat_number}")
                # Process payment securely
                transaction_id = PaymentSystem.process_payment(passenger, amount)
                print(f"Payment successful! Transaction ID: {transaction_id}")
                return True
            else:
                print(f"Seat {seat_number} is not available on Bus {bus_id}.")
                return False
        else:
            print(f"Bus {bus_id} or Passenger {username} does not exist in the system.")
            return False

# Example usage
reservation_system = ReservationSystem()

# Add passenger
reservation_system.add_passenger("ali_kaya", "Ali Kaya", "ali@gmail.com", "123456789")

# Authenticate passenger (in a real system, use a secure authentication mechanism)
reservation_system.authenticate_passenger("ali_kaya", "default_password")

# Add buses to the schedule
reservation_system.buses["A123"] = Bus("A123", "Mersin", "08:00", 20)

# Display bus schedule
reservation_system.buses["A123"].display_schedule()

# Make a reservation
reservation_system.make_reservation("A123", "ali_kaya", 5, 50)