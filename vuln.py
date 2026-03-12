import os

def run_command(user_input):
    # Intentional vulnerability (Command Injection) for testing SAST
    os.system(user_input)

def execute_code(code):
    # Intentional vulnerability (Eval) for testing SAST
    eval(code)
