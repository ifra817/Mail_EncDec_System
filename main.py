# main.py
import sys
import os
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox, QLineEdit, QTextEdit
from PyQt5.QtCore import QTimer, Qt
from gui import Ui_MainWindow
from cryptography_vernam import encrypt, decrypt, generate_random_key, evaluate_key_strength

class MainApp(QMainWindow, Ui_MainWindow):
    
    def __init__(self):

        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        bg_path = os.path.join(BASE_DIR, "IS_gui_bg.png")
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setStyleSheet(f"QMainWindow {{ background-image: url({bg_path}); background-repeat: no-repeat; background-position: center; }}")

        # Set the starting page to Loading page
        self.ui.stackedWidget.setCurrentWidget(self.ui.Loading_page)
        self.random_key = ""
        self.plaintext = ""
        self.subject = ""
        self.body = ""
        self.progress_value = 0
        self.last_operation = None  # Can be 'encrypt' or 'decrypt'


        # Create a timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_progress_bar)  # Call this function every timeout
        self.timer.start(30)  

        self.ui.Encryption_button.clicked.connect(lambda:self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.Decryption_button.clicked.connect(lambda:self.ui.stackedWidget.setCurrentIndex(3))
        
        self.ui.generate_key_button.clicked.connect(self.generate_key)
        self.ui.checkBox.stateChanged.connect(self.toggle_key_visibility)
        self.ui.Encrypt_Button.clicked.connect(self.encrypt_text)
        self.ui.clear_button.clicked.connect(self.clear_EncPage)

        self.ui.Decrypt_button.clicked.connect(self.decrypt_text)
        self.ui.clear_button_2.clicked.connect(self.clear_DecPage)

        self.ui.Back_button.clicked.connect(self.go_back)
        self.ui.exit_Button.clicked.connect(self.close)
        self.ui.Save_Button.clicked.connect(self.save_results)

    def update_progress_bar(self):
        self.progress_value += 1  # Increase progress value by 1
        self.ui.progressBar.setValue(self.progress_value)  # Set the progress bar value

        if self.progress_value >= 100:
            self.timer.stop()  # Stop the timer when progress is 100%
            self.ui.stackedWidget.setCurrentWidget(self.ui.EncryptOrDecrypt)

    def toggle_key_visibility(self, state):
        if state == Qt.Checked:
            self.ui.key_here.setEchoMode(QLineEdit.Normal)
        else:
            self.ui.key_here.setEchoMode(QLineEdit.Password)
    
    def clear_EncPage(self):
        self.ui.key_here.clear()
        self.ui.keyLength_here.clear()
        self.ui.subject.clear()
        self.ui.body.clear()

    def clear_DecPage(self):
        self.ui.CipherText_here.clear()
        self.ui.decryption_key.clear()


    def generate_key(self):
        subject_text = self.ui.subject.text()
        body_text = self.ui.body.toPlainText()
        plaintext = subject_text + body_text
        length = len(plaintext)

        try: 
            self.random_key = generate_random_key(length)
            self.ui.key_here.setText(self.random_key)
            self.ui.key_here.setEchoMode(QLineEdit.Password)
            self.ui.keyLength_here.setText(str(length))
        except Exception as e:
            QMessageBox.critical(self, "Key Generation Error", str(e))

    def encrypt_text(self):
        subject = self.ui.subject.text()
        body = self.ui.body.toPlainText()
        plaintext = subject+ "|||"+body
        key = self.random_key
        if not subject or not body or not key:
            QMessageBox.warning(self, "Error", "Email Subject and Body are required!")
            return
        print(f"Plaintext length: {len(plaintext)}, Key length: {len(key)}")

        try:
            encrypted = encrypt(plaintext, key)
            self.ui.result_here.setText(encrypted)
            self.ui.stackedWidget.setCurrentIndex(4)

            QMessageBox.information(
                self,
                "Encryption Successful",
                "Encryption completed!\n\n"
                "Ciphertext and Key have been generated.\n"
                "Please click the 'Save' button to store them safely.\n\n"
                "You will need them for decryption."
        )
            self.last_operation = 'encrypt'

        except Exception as e:
            QMessageBox.critical(self, "Encryption Error", str(e))

    def decrypt_text(self):
        ciphertext = self.ui.CipherText_here.toPlainText()
        key = self.ui.decryption_key.text()

        if not ciphertext or not key:
            QMessageBox.warning(self, "Error", "Ciphertext and Key are required!")
            return
        
        try:
            decrypted_text = decrypt(ciphertext, key)
            if "|||" in decrypted_text:
                subject_text, body_text = decrypted_text.split("|||", 1)  # split only at first "|||"
                final_output = (
                    f"Subject:\n{subject_text.strip()}\n\n"
                    f"Body:\n{body_text.strip()}"
                )
            else:
                final_output = decrypted_text

            self.ui.result_here.setText(final_output)
            self.ui.stackedWidget.setCurrentIndex(4)
            self.last_operation = 'decrypt'

        except Exception as e:
            QMessageBox.critical(self, "Decryption Error", str(e))

    def go_back(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def save_results(self):
        text_to_save = self.ui.result_here.toPlainText()
        if not text_to_save:
            QMessageBox.warning(self, "Warning", "There is no output to save!")
            return
        current_index = self.ui.stackedWidget.currentIndex()

        if current_index == 4:  # Result page (after encryption or decryption)
            if self.last_operation == 'encrypt':
                filename = "encrypted_emails.txt"
                content = (
                    "\n==== New Encrypted Email ====\n"
                    f"Ciphertext:\n{text_to_save}\n\n"
                    f"Key:\n{self.random_key}\n"
                    "------------------------------\n"
                )
            elif self.last_operation == 'decrypt':
                filename = "decrypted_emails.txt"
                used_key = self.ui.decryption_key.text()
                content = (
                    "\n==== New Decrypted Email ====\n"
                    f"Plaintext:\n{text_to_save}\n\n"
                    f"Key Used:\n{used_key}\n"
                    "------------------------------\n"
                )
            else:
                QMessageBox.warning(self, "Warning", "Unknown operation type. Cannot determine whether the result is encrypted or decrypted.")
                return


            try:
                with open(filename, 'a', encoding='utf-8') as file:
                    file.write(content)
                QMessageBox.information(
                    self,
                    "Saved Successfully",
                    f"Your data has been saved to '{filename}' in the current working directory.\n"
                    "Make sure to keep it safe!"
                )
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to save file: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())
