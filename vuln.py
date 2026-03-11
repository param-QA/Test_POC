import os
from flask import request

@app.route('/ping')
def ping():
    target = request.args.get('target')
    # Trigger: Executing shell commands with unsanitized user input
    os.system(f"ping -c 1 {target}")
