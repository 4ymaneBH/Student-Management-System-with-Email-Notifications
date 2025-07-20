Student Management System 🎓
🚀 Overview
The Student Management System is a Python-based application designed to streamline student data management. It generates random student data, displays it in a user-friendly GUI, and automates sending score reports via email. Built with simplicity and functionality in mind, this project is ideal for educators, administrators, or developers learning to integrate GUI, data generation, and email automation.
✨ Features

📝 Generate Random Students: Creates a CSV file with realistic student details (ID, name, scores, email) using the Faker library.
📊 Display Students: Loads student data from the CSV and presents it in a clean, tabular format within a Tkinter GUI.
📧 Send Emails: Automatically sends personalized score reports to students' email addresses using smtplib.
💾 Persistent Storage: Stores student data in a students.csv file for easy access and modification.
🖥️ User-Friendly Interface: Intuitive Tkinter GUI with buttons for generating data, displaying records, and sending emails.

🛠️ Technologies Used

Python 3.7+ 🐍: Core programming language for logic and scripting.
Tkinter 🖼️: Python's standard library for creating the graphical user interface.
Faker 🎭: Generates realistic fake data for student records.
CSV 📈: Stores student data in a simple, portable format.
smtplib ✉️: Handles email sending functionality.
email.mime 📄: Formats email content for professional delivery.

📥 Installation & Setup
Prerequisites

Python 3.7+: Download and install from python.org.
pip: Ensure Python's package manager is installed.
A Gmail account for email functionality (or another SMTP-compatible email provider).

Step 1: Clone the Repository
Clone the project to your local machine:
git clone https://github.com/yourusername/student-management-system.git
cd student-management-system

Step 2: Create a Virtual Environment
Using a virtual environment is recommended to isolate dependencies:
python -m venv env
# Activate virtual environment
# On macOS/Linux:
source env/bin/activate
# On Windows:
env\Scripts\activate

Step 3: Install Dependencies
Install required Python packages listed in requirements.txt:
pip install -r requirements.txt


Note: Tkinter is included in Python's standard library, so no separate installation is needed for it.

Step 4: Configure Email Credentials
To enable email functionality, configure your email credentials in main.py:
EMAIL_ADDRESS = "your_email@gmail.com"  # Replace with your Gmail address
EMAIL_PASSWORD = "your_app_password"   # Replace with your App Password


⚠️ Important: For Gmail, you must:

Enable 2-Step Verification in your Google Account.
Generate an App Password via Google Account Settings.
Use the App Password instead of your regular password to avoid security issues.
Alternatively, if using another email provider, update the SMTP server settings (host, port) in main.py.


Step 5: Verify Setup
Ensure all dependencies are installed correctly:
pip list

Check for faker, and ensure Python includes tkinter, smtplib, and email.
🎮 Usage
Running the Application
Start the application by running the main script:
python main.py

GUI Functionality
The Tkinter GUI provides three main options:

Generate Student Data 📝: Creates a students.csv file with random student records (e.g., ID, name, email, scores in Math, Science, and English).
Display Students 📊: Loads the students.csv file and displays the data in a table within the GUI.
Email Scores 📧: Sends each student an email with their scores, using the configured email credentials.


Tip: Ensure students.csv exists before displaying or emailing data. If it doesn't, use the "Generate Student Data" option first.

Example Workflow

Run python main.py.
Click "Generate Student Data" to create students.csv.
Click "Display Students" to view the data in the GUI.
Click "Email Scores" to send score reports to students' email addresses.

📂 File Structure
student-management-system/
├── students.csv          # Generated CSV file with student data
├── main.py              # Main application script with GUI and logic
├── requirements.txt      # List of Python dependencies
├── README.md            # Project documentation (this file)
└── env/                 # Virtual environment folder (not tracked in Git)

📋 Requirements File (requirements.txt)
The requirements.txt ensures consistent dependency versions:
faker==28.1.0


Note: Tkinter, smtplib, and email are part of Python's standard library and don't need to be listed in requirements.txt.

🧑‍💻 Example Code Snippet
Below is a simplified example of how main.py might structure the email-sending functionality:
import smtplib
from email.mime.text import MIMEText

def send_email(student, scores):
    msg = MIMEText(f"Dear {student['name']},\nYour scores: {scores}")
    msg['Subject'] = 'Your Academic Scores'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = student['email']
    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)

For the full implementation, refer to main.py.
🤝 Contributing
Contributions are welcome! To contribute:

Fork the repository.
Create a new branch (git checkout -b feature/your-feature).
Make your changes and commit (git commit -m "Add your feature").
Push to the branch (git push origin feature/your-feature).
Open a Pull Request on GitHub.

Suggestions for improvements:

Add support for multiple CSV formats or database integration (e.g., SQLite).
Enhance the GUI with themes or additional data visualization.
Implement error handling for invalid email addresses.

📜 License
This project is licensed under the MIT License.
❓ FAQs
Q: Why am I getting an SMTP authentication error?A: Ensure you've used an App Password for Gmail (not your regular password) and that 2-Step Verification is enabled.
Q: Can I use a different email provider?A: Yes, update the SMTP server settings (host, port) and credentials in main.py to match your provider.
Q: What if Tkinter is not found?A: Ensure you're using a Python version with Tkinter included. For Ubuntu, install it with sudo apt-get install python3-tk.
📬 Contact
For questions or support, open an issue on GitHub or contact [yourusername]@email.com.

🌟 Happy Managing! 🌟
