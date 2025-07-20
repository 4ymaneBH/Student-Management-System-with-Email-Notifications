# Student Management System

## Overview

The Student Management System is a Python-based application designed to simplify student data management. It generates random student records, displays them in a user-friendly GUI, and automates sending score reports via email. Perfect for educators, administrators, or developers exploring GUI, data generation, and email automation, this project combines simplicity with practical functionality.

## Features

- **Generate Random Students**: Creates a `students.csv` file with realistic student details (ID, name, scores, email) using Faker
- **Display Students**: Loads and presents student data in a tabular format within a Tkinter GUI
- **Send Emails**: Automatically emails personalized score reports to students using smtplib
- **Persistent Storage**: Saves student data in a CSV file for easy access and modification
- **User-Friendly Interface**: Intuitive Tkinter GUI with buttons for generating, displaying, and emailing data

## Technologies Used

- **Python 3.7+**: Core programming language for logic and scripting
- **Tkinter**: Python's standard library for building the graphical interface
- **Faker**: Generates realistic fake data for student records
- **CSV**: Stores student data in a portable, structured format
- **smtplib**: Handles email sending functionality
- **email.mime**: Formats professional email content

## Installation & Setup

### Prerequisites

- **Python 3.7+**: Download from [python.org](https://python.org)
- **pip**: Python's package manager (included with Python)
- A Gmail account or another SMTP-compatible email provider for sending emails

### Step 1: Clone the Repository

Clone the project to your local machine:

```bash
git clone https://github.com/yourusername/student-management-system.git
cd student-management-system
```

### Step 2: Create a Virtual Environment

Isolate dependencies using a virtual environment:

```bash
python -m venv env

# Activate virtual environment
# On macOS/Linux:
source env/bin/activate

# On Windows:
env\Scripts\activate
```

### Step 3: Install Dependencies

Install required packages from requirements.txt:

```bash
pip install -r requirements.txt
```

> **Note**: Tkinter, smtplib, and email are part of Python's standard library and do not require separate installation.

### Step 4: Configure Email Credentials

Update `main.py` with your email credentials for sending score reports:

```python
EMAIL_ADDRESS = "your_email@gmail.com"  # Replace with your Gmail address
EMAIL_PASSWORD = "your_app_password"    # Replace with your App Password
```

> ⚠️ **Gmail Setup**:
> - Enable 2-Step Verification in your Google Account Settings
> - Generate an App Password for secure access
> - Use the App Password in `main.py` instead of your regular password
> - For non-Gmail providers, update the SMTP server settings (host, port) in `main.py`

### Step 5: Verify Installation

Check that dependencies are installed:

```bash
pip list
```

Ensure `faker` is listed, and verify Tkinter is available by running:

```bash
python -c "import tkinter"
```

## Usage

### Running the Application

Launch the application:

```bash
python main.py
```

### GUI Functionality

The Tkinter interface offers three main features:

1. **Generate Student Data**: Creates a `students.csv` file with random student records (e.g., ID, name, email, Math, Science, English scores)
2. **Display Students**: Loads `students.csv` and shows data in a table within the GUI
3. **Email Scores**: Sends personalized score reports to students' email addresses

> **Tip**: Generate student data first to create `students.csv` before using the display or email features.

### Example Workflow

1. Run `python main.py`
2. Click **Generate Student Data** to create `students.csv`
3. Click **Display Students** to view records in the GUI
4. Click **Email Scores** to send score reports to students

## File Structure

```
student-management-system/
├── students.csv          # Generated CSV file with student data
├── main.py              # Main script with GUI and logic
├── requirements.txt      # Python package dependencies
├── README.md            # Project documentation (this file)
└── env/                 # Virtual environment folder (not tracked in Git)
```

## Requirements File (requirements.txt)

```
faker==28.1.0
```

> **Note**: Tkinter, smtplib, and email are included in Python's standard library.

## Example Code Snippet

Below is a simplified example of the email-sending function in `main.py`:

```python
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
```

Refer to `main.py` for the complete implementation.

## Contributing

Contributions are encouraged! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m "Add your feature"`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request on GitHub

### Ideas for Improvement:

- Add support for database storage (e.g., SQLite) instead of CSV
- Enhance the GUI with themes, sorting, or filtering options
- Implement robust error handling for email failures or invalid data

## License

This project is licensed under the MIT License.

## FAQs

**Q: Why am I getting an SMTP authentication error?**  
A: Verify that you're using an App Password for Gmail and that 2-Step Verification is enabled. Check your email and password in `main.py`.

**Q: Can I use a different email provider?**  
A: Yes, modify the SMTP server settings (host, port) and credentials in `main.py` to match your provider's requirements.

**Q: What if Tkinter is not found?**  
A: Ensure Python includes Tkinter. On Ubuntu, install it with `sudo apt-get install python3-tk`. On Windows/macOS, Tkinter is typically included.

**Q: How can I customize the student data?**  
A: Modify the data generation logic in `main.py` to include additional fields or adjust score ranges.

## Contact

For questions, bug reports, or suggestions, open an issue on GitHub or email [yourusername]@email.com.

**Happy Managing!** 🎓
