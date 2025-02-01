import csv
import random
import smtplib
from tkinter import *
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from faker import Faker

# Initialize Faker with Moroccan localization
fake = Faker('fr_FR')

# Email configurations
EMAIL_ADDRESS = "your_email@gmail.com"  # Replace with your email address
EMAIL_PASSWORD = "your_password"  # Replace with your email password

# CSV File Path
CSV_FILE = "students.csv"

# Generate random student data
def generate_students_csv(num_students=10):
    headers = ["Student ID", "Name", "Math", "Physics", "English", "Total Score", "Email"]
    with open(CSV_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        for _ in range(num_students):
            student_id = fake.unique.random_int(min=1000, max=9999)
            name = fake.name()
            math = random.randint(0, 100)
            physics = random.randint(0, 100)
            english = random.randint(0, 100)
            total_score = math + physics + english
            email = fake.email()
            writer.writerow([student_id, name, math, physics, english, total_score, email])
    print(f"Generated {num_students} students in '{CSV_FILE}'")

# Send email to student
def send_email(to_email, student_name, scores):
    try:
        message = MIMEMultipart()
        message['From'] = EMAIL_ADDRESS
        message['To'] = to_email
        message['Subject'] = "Your Course Scores"
        
        # Create email body
        body = f"Hello {student_name},\n\nYour course scores are as follows:\n"
        for subject, score in scores.items():
            body += f"{subject}: {score}\n"
        body += f"\nTotal Score: {scores['Total Score']}\n\nBest of luck with your studies!\n\n"
        message.attach(MIMEText(body, 'plain'))
        
        # Send email
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(message)
            print(f"Email sent to {student_name} at {to_email}")
    except Exception as e:
        print(f"Failed to send email to {student_name}: {e}")

# GUI and Main Functionality
root = Tk()
root.geometry("800x600")
root.title("Student Management System")

# GUI Elements for Score Display
lbl_title = Label(root, text="Student Management System", font=('aria', 30, 'bold'), fg="steel blue")
lbl_title.pack()

# Load CSV and display students in a table
def display_students():
    with open(CSV_FILE, mode='r') as file:
        reader = csv.reader(file)
        for i, row in enumerate(reader):
            for j, col in enumerate(row):
                label = Label(root, text=col, font=('aria', 12), bg="lightgrey" if i == 0 else "white", padx=5, pady=5)
                label.grid(row=i+2, column=j)

def calculate_score_and_email():
    with open(CSV_FILE, mode='r') as file:
        reader = csv.reader(file)
        headers = next(reader)  # skip headers
        for row in reader:
            student_id, name, math, physics, english, total_score, email = row
            scores = {
                "Math": int(math),
                "Physics": int(physics),
                "English": int(english),
                "Total Score": int(total_score)
            }
            send_email(email, name, scores)

# Generate student data on button click
btn_generate_data = Button(root, text="Generate Student Data", font=('aria', 14, 'bold'), bg="powder blue", command=generate_students_csv)
btn_generate_data.pack(pady=10)

# Display student data button
btn_display_data = Button(root, text="Display Students", font=('aria', 14, 'bold'), bg="powder blue", command=display_students)
btn_display_data.pack(pady=10)

# Calculate and email scores button
btn_email_scores = Button(root, text="Email Scores", font=('aria', 14, 'bold'), bg="powder blue", command=calculate_score_and_email)
btn_email_scores.pack(pady=10)

root.mainloop()
