import subprocess
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QWidget, QMessageBox


class WiFiPasswordViewer(QMainWindow):
    def __init__(self):
        super().__init__()

        # Window settings
        self.setWindowTitle("Wi-Fi Password Viewer")
        self.setGeometry(200, 200, 600, 400)

        # Main layout
        self.main_widget = QWidget()
        self.layout = QVBoxLayout(self.main_widget)
        self.setCentralWidget(self.main_widget)

        # Table to display Wi-Fi names and passwords
        self.table = QTableWidget(0, 2)
        self.table.setHorizontalHeaderLabels(["Wi-Fi Name", "Password"])
        self.layout.addWidget(self.table)

        # Button to fetch Wi-Fi passwords
        self.fetch_button = QPushButton("Fetch Wi-Fi Passwords")
        self.fetch_button.clicked.connect(self.fetch_passwords)
        self.layout.addWidget(self.fetch_button)

    def fetch_passwords(self):
        try:
            # Get the list of Wi-Fi profiles
            data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'])
            data = data.decode('utf-8').split('\n')
            profiles = [line.split(":")[1][1:-1] for line in data if "All User Profile" in line]

            # Clear existing table rows
            self.table.setRowCount(0)

            # Fetch passwords for each profile
            for profile in profiles:
                try:
                    profile_data = subprocess.check_output(
                        ['netsh', 'wlan', 'show', 'profile', profile, 'key=clear']
                    )
                    profile_data = profile_data.decode('utf-8').split('\n')
                    password = [line.split(":")[1][1:-1] for line in profile_data if "Key Content" in line]
                    password = password[0] if password else "None"
                except subprocess.CalledProcessError:
                    password = "Error retrieving"

                # Add data to the table
                row_position = self.table.rowCount()
                self.table.insertRow(row_position)
                self.table.setItem(row_position, 0, QTableWidgetItem(profile))
                self.table.setItem(row_position, 1, QTableWidgetItem(password))

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to fetch Wi-Fi passwords.\n{e}")


# Main application
if __name__ == "__main__":
    app = QApplication([])

    # Initialize and display the window
    viewer = WiFiPasswordViewer()
    viewer.show()

    app.exec()