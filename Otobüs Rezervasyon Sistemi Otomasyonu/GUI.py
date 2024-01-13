import tkinter as tk
from tkinter import messagebox

class BusReservationSystem:
    def __init__(self, master):
        self.master = master
        self.master.title("Bus Reservation System")

        # Create and configure widgets
        self.create_widgets()

    def create_widgets(self):
        # Making a Ticket Reservation
        reservation_frame = tk.Frame(self.master)
        reservation_frame.pack(pady=10)
        tk.Label(reservation_frame, text="Making a Ticket Reservation").pack()

        tk.Button(reservation_frame, text="Display Schedules", command=self.display_schedules).pack()
        tk.Button(reservation_frame, text="Make Reservation", command=self.make_reservation).pack()

        # Seat Selection and Arrangement
        seat_frame = tk.Frame(self.master)
        seat_frame.pack(pady=10)
        tk.Label(seat_frame, text="Seat Selection and Arrangement").pack()

        tk.Button(seat_frame, text="Choose Seat", command=self.choose_seat).pack()

        # Passenger Information Update
        info_frame = tk.Frame(self.master)
        info_frame.pack(pady=10)
        tk.Label(info_frame, text="Pasanger Information Update").pack()

        tk.Button(info_frame, text="Login and Update Info", command=self.update_information).pack()

        # Bus Expedition Planning
        planning_frame = tk.Frame(self.master)
        planning_frame.pack(pady=10)
        tk.Label(planning_frame, text="Bus Expedition Planning").pack()

        tk.Button(planning_frame, text="Plan New Bus Service", command=self.plan_new_service).pack()

        # Making Payments and Tracking Transactions
        payment_frame = tk.Frame(self.master)
        payment_frame.pack(pady=10)
        tk.Label(payment_frame, text="Making Payments and Tracking Transactions").pack()

        tk.Button(payment_frame, text="Pay for Ticket", command=self.pay_for_ticket).pack()

        # Receive Notification
        notification_frame = tk.Frame(self.master)
        notification_frame.pack(pady=10)
        tk.Label(notification_frame, text="Receive Notification").pack()

        tk.Button(notification_frame, text="Receive Notifications", command=self.receive_notifications).pack()

        # Viewing Income Reports
        income_frame = tk.Frame(self.master)
        income_frame.pack(pady=10)
        tk.Label(income_frame, text="Viewing Income Reports").pack()

        tk.Button(income_frame, text="View Income Reports", command=self.view_income_reports).pack()

        # Security Check
        security_frame = tk.Frame(self.master)
        security_frame.pack(pady=10)
        tk.Label(security_frame, text="Security Check").pack()

        tk.Button(security_frame, text="Security Check", command=self.security_check).pack()

        # Collecting Improvement Feedback
        feedback_frame = tk.Frame(self.master)
        feedback_frame.pack(pady=10)
        tk.Label(feedback_frame, text="Collecting Improvement Feedback").pack()

        tk.Button(feedback_frame, text="Provide Feedback", command=self.provide_feedback).pack()

    def display_schedules(self):
        messagebox.showinfo("Display Schedules", "Displaying Passenger Bus Schedules")

    def make_reservation(self):
        messagebox.showinfo("Make Reservation", "Making a Ticket Reservation")

    def choose_seat(self):
        messagebox.showinfo("Choose Seat", "Seat Selection and Arrangement")

    def update_information(self):
        messagebox.showinfo("Update Information", "Login and Update Personal Information")

    def plan_new_service(self):
        messagebox.showinfo("Plan New Service", "Planning, Organizing, or Adding New Bus Service")

    def pay_for_ticket(self):
        messagebox.showinfo("Pay for Ticket", "Paying for the Ticket")

    def receive_notifications(self):
        messagebox.showinfo("Receive Notifications", "Receiving Notifications about Bus Schedules")

    def view_income_reports(self):
        messagebox.showinfo("View Income Reports", "Viewing Revenue Reports from Bus Trips")

    def security_check(self):
        messagebox.showinfo("Security Check", "Performing Security Check")

    def provide_feedback(self):
        messagebox.showinfo("Provide Feedback", "Providing Feedback for System Improvement")


def main():
    root = tk.Tk()
    app = BusReservationSystem(root)
    root.mainloop()

if __name__ == "__main__":
    main()