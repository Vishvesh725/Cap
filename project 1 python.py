# Sample implementation of an Attendance Management System

# Dummy data for user authentication (Replace with a database)
users = {
    "admin": "admin123",
    "teacher": "teacher123",
}

# Dummy data for student/employee information (Replace with a database)
students = {
    1: {"name": "John Doe", "attendance": {}},
    2: {"name": "Jane Smith", "attendance": {}},
    # Add more students here
}

# Function to handle user login
def login():
    username = input("Username: ")
    password = input("Password: ")
    if username in users and users[username] == password:
        return True
    return False

# Function to mark attendance
def mark_attendance(student_id):
    if student_id in students:
        date = input("Enter date (YYYY-MM-DD): ")
        if date not in students[student_id]["attendance"]:
            students[student_id]["attendance"][date] = "Present"
            print("Attendance marked successfully!")
        else:
            print("Attendance already marked for this date.")
    else:
        print("Student not found.")

# Function to generate attendance report
def generate_report(student_id):
    if student_id in students:
        print(f"Attendance Report for {students[student_id]['name']}")
        for date, status in students[student_id]["attendance"].items():
            print(f"{date}: {status}")
    else:
        print("Student not found.")

# Main function
def main():
    print("Attendance Management System")
    if login():
        print("Login successful!")
        while True:
            print("\nMenu:")
            print("1. Mark Attendance")
            print("2. Generate Report")
            print("3. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                student_id = int(input("Enter student ID: "))
                mark_attendance(student_id)
            elif choice == "2":
                student_id = int(input("Enter student ID: "))
                generate_report(student_id)
            elif choice == "3":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
