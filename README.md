# user-management-system

This is a simple desktop application for managing users using Tkinter and SQLite in Python. The application allows users to add, delete, and view users in a SQLite database. The user interface is built with Tkinter and includes features to interact with the user data.

## Features

- **Add User**: Insert a new user into the database by providing a name and email.
- **Delete User**: Remove a user from the database using their ID.
- **View Users**: Display all users in the database in a table format.

## Prerequisites

Python installed: Ensure Python is installed on your machine. You can download it from python.org.
Tkinter included: Tkinter comes pre-installed with most Python installations, but if you're using a minimal version of Python, you can install it using:

- sudo apt-get install python3-tk
  (For Linux users) or via your OS package manager.

Steps to Run on Windows:

Install Python:
   If you don't have Python installed, download and install it from python.org.
   During installation, make sure to check the box "Add Python to PATH" so you can run Python from the command prompt.
   
- Python 3.x
- Tkinter (usually included with Python installation)
- SQLite (usually included with Python installation)

## Installation

1. **Clone the Repository**

   If you're using Git, you can clone the repository with:
   ```sh
   git clone https://github.com/mashudu2021/user-management-system.git
   cd user-management-system


Steps to Run the Code:
Save the Code:

Save the Python code into a file. For example, name the file user_management_system.py.
Run the Script:

Open a terminal or command prompt.
Navigate to the folder where the script is saved.
Run the script with the following command:
bash
Copy code
python tkin.py
If you're using Python 3, use:

bash
Copy code
python3 tkin.py
Explanation of What Will Happen:
A GUI window will open, allowing you to add users by entering a name and email.

![user management](https://github.com/user-attachments/assets/ff5d93f0-21ae-4aad-985f-f2eef802193f)


You can delete a user by entering their ID and clicking the "Delete User" button.
The users are displayed in the Treeview widget, which shows the user ID, name, and email.
The Refresh List button will refresh the list of users after any changes.
