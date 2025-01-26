# File: vulnerable_script.py
"""
Validate best practices using GitHub Actions.

This script will check the result of the action.
"""

import os

# Explicitly hardcoded sensitive data
API_KEY = os.environ.get("API_KEY") 
SECRET_KEY = os.environ.get("SECRET_KEY")
password = os.environ.get("PASSWORD")

def connect_to_service():
    """
    Connect to a service using API keys.

    This function does not take any inputs and only prints a connection message.
    """
    print(f"Connecting with API key: {API_KEY} and secret: {SECRET_KEY}")
