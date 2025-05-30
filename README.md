# Mail_EncDec_System 🔐✉️

A Python-based GUI application to **encrypt** and **decrypt** emails using the **Vernam Cipher**.  
This tool allows users to input an email's **subject and body**, generate a one-time key, encrypt/decrypt messages, and **safely store** results.

---

## 🚀 Features

- 🗝️ Vernam Cipher implementation for strong symmetric encryption.
- 🧠 Random key generation based on input length.
- 📧 Structured input fields for email **Subject** and **Body**.
- 🔒 Option to hide/show encryption keys.
- 💾 Save encrypted/decrypted messages to `.txt` files.
- 🎨 PyQt5-based GUI with loading screen and navigation.
- 🖼️ Background image support (path handled dynamically).
- 🔍 Key strength evaluator (optional enhancement).

---

## 🧪 Tech Stack & Tools

- Python 3.x

- PyQt5 (GUI framework)

- Qt Designer (GUI design tool, .ui to .py conversion)

- VS Code (code editor)

- **Libraries Used:**
  - `PyQt5.QtWidgets` – GUI components
  - `PyQt5.QtCore` – Core functionality like `QTimer`, `Qt`
  - `os`, `sys` – System operations
  - `gui` – Auto-generated from Qt Designer
  - `cryptography_vernam` – Your custom module for encryption

---

## 🖥️ Installation & Setup

1. **Clone this repository:**

   ```bash
   git clone https://github.com/your-username/Mail_EncDec_System.git
   
   cd Mail_EncDec_System
   ```

2. **Install dependencies:**
   
   ```bash
   pip install PyQt5
   ```

3. **Run the application:**

   ```bash
   python main.py
   ```

---

## Project Interface

![image](https://github.com/user-attachments/assets/9d6f77ba-8d03-4103-81c8-6d6ccd4da849)

---

## 📂 Project Structure

  ```pgsql
  Mail_EncDec_System/
  ├── IS_gui_bg.png                   # GUI background image
  ├── main.py                 # Main entry point with GUI logic
  ├── gui.py                  # Converted UI layout (from Qt Designer)
  ├── cryptography_vernam.py  # Core logic for Vernam encryption/decryption & key generation
  ├── encrypted_emails.txt    # Output file for encrypted messages
  ├── decrypted_emails.txt    # Output file for decrypted messages
  └── README.md               # Project documentation
```

---

## 🧑‍💻  Usage Guide

  1. Launch the application using python main.py.
  
  2. Select an option (Encrypt/Decrypt).
 
  3. To Encrypt:

     - Enter the Subject and Body of your email.
    
     - Press Generate Key.
    
     - Click Encrypt to secure the content.
    
     - Save the encrypted output and key for later use.

  4. To Decrypt:
     
      - Paste the encrypted message and corresponding key.

      - Click Decrypt to reveal the original content.
      
      - Save the decrypted output.

---
    
## 🛡️ Security Note

- The Vernam Cipher is theoretically unbreakable only when the key is:

    - Truly random
    
    - As long as the message
    
    - Used only once (one-time pad)

- This tool provides a simulation and is intended for educational or internal-use scenarios.

- Secure key exchange and storage should be handled externally for sensitive use.

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change or add.

---

## 📬 Contact

For feedback, suggestions, or collaboration opportunities, feel free to reach out:

- 👩‍💻 Developer: Ifra Ahmed

- 📧 Email: ifraahmed817@gmail.com








