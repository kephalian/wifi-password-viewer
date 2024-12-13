# wifi-password-viewer
Lookup all saved wifi passwords on a Windows system Needs Administrator privileges 

# Wi-Fi Password Viewer

A Python application that retrieves saved Wi-Fi passwords on a Windows system and displays them in a user-friendly GUI built with PySide6.


---

Features

Retrieves all saved Wi-Fi profiles on a Windows machine.

Displays Wi-Fi names and their corresponding passwords in a dynamic table.

Simple and intuitive GUI with a button to fetch the latest Wi-Fi information.

Handles errors gracefully and provides feedback to the user.



---

Requirements

Operating System: Windows (Administrator privileges required).

Python: 3.8 or later.

Dependencies:
Install the following Python packages:

pip install PySide6



---

Usage

1. Clone the repository:

git clone 
https://github.com/kephalian/wifi-password-viewer/tree/main

2. Run the script:

python wifi_password_viewer.py


3. Fetch Wi-Fi Passwords:

Click the "Fetch Wi-Fi Passwords" button in the application.

The table will display saved Wi-Fi names and passwords.





---

Code Explanation

1. Main Functionality:

Uses the netsh Windows command to retrieve Wi-Fi profiles and their passwords.

Extracts and decodes the output to parse profile names and passwords.



2. GUI:

Built with PySide6, featuring a table (QTableWidget) to display data and a button (QPushButton) to fetch the passwords.



3. Error Handling:

Handles subprocess errors and displays messages using QMessageBox if something goes wrong.





---

Example Output


---

License

This project is licensed under the MIT License. See the LICENSE file for details.


---

Disclaimer

This script is designed for educational purposes and should only be used on systems you own or have explicit permission to access. Misuse of this script may violate laws or terms of service. Use responsibly!


---

Feel free to modify or contribute to the project. Let me know if additional details are required!

