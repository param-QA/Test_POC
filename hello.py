import os
import requests

# VULNERABILITY 1: Hardcoded AWS Credentials (detected by Trivy/Semgrep)
AWS_ACCESS_KEY_ID = "AKIA5S67890EXAMPLE12"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

def download_backup(user_input_url):
    # VULNERABILITY 2: Command Injection (detected by Semgrep/Opengrep)
    # If a user provides "google.com; rm -rf /", this will execute the delete command.
    print(f"Downloading from {user_input_url}...")
    os.system("wget " + user_input_url)

def login_to_service():
    # VULNERABILITY 3: Hardcoded Password in a request
    payload = {
        "username": "admin",
        "password": "password123!"
    }
    response = requests.post("https://api.internal.service/login", data=payload)
    return response.status_code

if __name__ == "__main__":
    url = input("Enter backup URL: ")
    download_backup(url)
