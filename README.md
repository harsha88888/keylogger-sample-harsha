# keylogger-sample-harsha
# 🔐 Python Keylogger (Educational Use Only)

This is a modular **Python keylogger tool** developed for **educational and ethical hacking purposes** only. It includes multiple monitoring features, stealth functionality, and email reporting.

## 📁 Features

- 🔑 Keystroke logging
- 🖱️ Mouse movement and click logging
- 📋 Clipboard monitoring
- 🖼️ Screenshot capturing
- 🎤 Microphone recording
- 📧 Email reporting
- 🧿 Active window/app tracking
- 🕵️ Stealth mode (hidden console window)
- 🛡️ Anti-VM detection
- 🔄 Persistence across reboots
- 🔐 File encryption

---

## ⚙️ Requirements

Create a `requirements.txt` file with the following:

```txt
pynput
pyperclip
Pillow
sounddevice
scipy
numpy
pycryptodome
psutil
Install them using:

pip install -r requirements.txt
▶️ How to Run
(use python name of file.py)
windows+r and change to its respective directory and start running.
⚠️ Only run on your own system in a controlled or test environment. Do not run on others' devices without consent.

✅ Clone or Download the repository:

git clone https://github.com/harsha88888/keylogger-sample-harsha.git
cd keylogger-sample-harsha
✅ Install dependencies:

pip install -r requirements.txt
✅ Edit your email settings in email_sender.py:

python

EMAIL_ADDRESS = "your_email@example.com"
EMAIL_PASSWORD = "your_password_or_app_password"
✅ Start the program:

python main.py

#to stop 🔴 If you ran it from Terminal / Command Prompt:
✅ Windows:
Press Ctrl + C in the terminal window where the script is running.

This stops the process.

Or run this in a new Command Prompt:

c
Copy
Edit
tasklist | findstr python
Then:

cmd
Copy
Edit
taskkill /F /IM python.exe
✅ Linux / Mac:
In terminal where the script is running:
Ctrl + C
Or:
ps aux | grep python
Then:
kill -9 <PID>
🧹 If it's running in the background (via persistence or stealth):
Check for the following and delete:

📁 1. Startup Folder (Windows):
Open:
shell:startup
Delete any .py, .exe, or suspicious file added there.
🔍 2. Task Scheduler (Windows):
Open Task Scheduler → Look under "Task Scheduler Library"
Delete any suspicious tasks
📄 3. Windows Registry:
Open regedit
Navigate to:
mathematica
HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run
Remove any suspicious value related to your script name.
🧪 Optional: Check if running silently in the background
Use this command to identify Python processes:
cmd
wmic process where "name like '%python%'" get ProcessId,CommandLine
Then use:
cmd
taskkill /PID <PID> /F

🛑 Legal Disclaimer
This software is intended only for educational, ethical hacking, and security research purposes. Unauthorized use, distribution, or deployment of this software on devices you do not own or have permission to test on is strictly prohibited and may be punishable under law.

You are solely responsible for using this tool legally.

