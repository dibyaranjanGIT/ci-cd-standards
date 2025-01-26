# File: vulnerable_script.py
"""
Validate best practices using GitHub Actions.

This script will check the result of the action.
"""

import json
import os
import sys
from collections import defaultdict
from database.models import User
from datetime import datetime
from flask import Flask
from math import sqrt
from services.calculator import calculate_area
from utils.helper import format_date

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
