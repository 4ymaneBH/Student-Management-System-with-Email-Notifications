# Student Management System

## Overview
This Python-based **Student Management System** allows users to generate random student data, display it in a GUI, and send automated emails with students' scores. The system uses **Tkinter** for the graphical interface, **Faker** for generating random student data, and **smtplib** for email functionality.

## Features
- **Generate Random Students:** Creates a CSV file with random student details (ID, name, scores, email, etc.).
- **Display Students:** Loads and presents the student data in a structured table format.
- **Send Emails:** Automatically emails students their scores.

## Technologies Used
- **Python** (Core programming language)
- **Tkinter** (GUI for displaying students)
- **CSV** (To store student data)
- **Faker** (Generates fake student details)
- **smtplib** (Sends email notifications)
- **email.mime** (Formats email messages)

## Installation & Setup

### Prerequisites
Ensure you have Python installed (>=3.7). You can download it from [python.org](https://www.python.org/downloads/).

### Step 1: Clone the Repository
```sh
 git clone https://github.com/yourusername/student-management-system.git
 cd student-management-system
```

### Step 2: Create a Virtual Environment (Recommended)
```sh
python -m venv env  # Create virtual environment
source env/bin/activate  # Activate on Mac/Linux
env\Scripts\activate  # Activate on Windows
```

### Step 3: Install Dependencies
```sh
pip install -r requirements.txt
```

### Step 4: Set Up Email Credentials
Update the following variables in `main.py` with your **Gmail credentials**:
```python
EMAIL_ADDRESS = "your_email@gmail.com"  # Replace with your email
EMAIL_PASSWORD = "your_password"  # Replace with your password
```
> **Note:** If using Gmail, enable "Less Secure Apps" or use an App Password.

## Usage

### Run the Application
```sh
python main.py
```

### GUI Options:
1. **Generate Student Data** – Creates a `students.csv` file with random students.
2. **Display Students** – Loads and shows students in a table format.
3. **Email Scores** – Sends student scores to their email addresses.

## File Structure
```
student-management-system/
│── students.csv       # Auto-generated student data
│── main.py            # Main script
│── requirements.txt   # Dependencies
│── README.md          # Project documentation
```

## Requirements File (`requirements.txt`)
```
tkinter
faker
smtplib
email
```

## Contributing
Feel free to contribute by creating a pull request or suggesting improvements.

## License
This project is licensed under the MIT License.

