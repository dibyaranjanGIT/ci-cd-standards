# File: vulnerable_script.py
"""
Validate best practices using GitHub Actions.

This script will check the result of the action.
"""

# Explicitly hardcoded sensitive data
API_KEY = "AIzaSyD-EXAMPLE1234567890abcdefgHIJKLM"
SECRET_KEY = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"
password = "P@ssw0rd123!"

def connect_to_service():
    """
    Connect to a service using API keys.

    This function does not take any inputs and only prints a connection message.
    """
    print(f"Connecting with API key: {API_KEY} and secret: {SECRET_KEY}")
