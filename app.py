# File: vulnerable_script.py
"""
Validate best practics using github actions.
Will check result of action.
"""
# Explicitly hardcoded sensitive data
API_KEY = "AIzaSyD-EXAMPLE1234567890abcdefgHIJKLM"
SECRET_KEY = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"
password="P@ssw0rd123!"

def connect_to_service():
    """
    Add function to connect to servie.
    No input only print function.
    """
    print(f"Connecting with API key: {API_KEY} and secret: {SECRET_KEY}")
