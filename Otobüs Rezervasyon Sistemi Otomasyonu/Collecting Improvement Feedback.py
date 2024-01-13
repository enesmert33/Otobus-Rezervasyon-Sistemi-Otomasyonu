class FeedbackSystem:
    def __init__(self):
        self.feedback_data = {}

    def collect_feedback(self, username, feedback_text):
        if username not in self.feedback_data:
            self.feedback_data[username] = []
        self.feedback_data[username].append(feedback_text)
        print(f"Feedback collected from {username}: {feedback_text}")

    def evaluate_feedback(self):
        # Perform analysis on collected feedback
        # For simplicity, let's assume the analysis identifies common issues
        common_issues = ["Slow website", "Confusing reservation process"]
        return common_issues

    def implement_improvements(self, improvements):
        if improvements:
            print("\nImplementing improvements:")
            for improvement in improvements:
                print(f"- {improvement}")
            print("Continuous improvements implemented successfully.")
        else:
            print("No improvements to implement at this time.")

    def view_feedback(self, username):
        if username in self.feedback_data:
            print(f"\nFeedback from {username}:")
            for feedback in self.feedback_data[username]:
                print(f"- {feedback}")
        else:
            print(f"No feedback available from {username}.")

class BusReservationSystem:
    def __init__(self):
        self.feedback_system = FeedbackSystem()
        self.improvements = []

    def collect_and_evaluate_feedback(self, username, feedback_text):
        self.feedback_system.collect_feedback(username, feedback_text)
        common_issues = self.feedback_system.evaluate_feedback()
        self.improvements.extend(common_issues)

    def implement_continuous_improvements(self):
        self.feedback_system.implement_improvements(self.improvements)
        self.improvements = []

# Example usage:
bus_system = BusReservationSystem()

# Collect and evaluate feedback
bus_system.collect_and_evaluate_feedback("ali_kaya", "The reservation process was confusing.")
bus_system.collect_and_evaluate_feedback("ahmet_mutlu", "The website was slow and unresponsive.")

# View feedback
bus_system.feedback_system.view_feedback("ali_kaya")
bus_system.feedback_system.view_feedback("ahmet_mutlu")

# Implement continuous improvements
bus_system.implement_continuous_improvements()