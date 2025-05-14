from flask import Flask, request, jsonify
import os
import requests
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Replace with your Smarty API credentials
SMARTY_AUTH_ID = os.environ.get("SMARTY_AUTH_ID")
SMARTY_AUTH_TOKEN = os.environ.get("SMARTY_AUTH_TOKEN")
if not SMARTY_AUTH_ID or not SMARTY_AUTH_TOKEN:
    raise ValueError("SMARTY auth is not set in environment variables.")

def validate_address_smartystreets(street, city, state, zipcode):
    params = {
        'auth-id': SMARTY_AUTH_ID,
        'auth-token': SMARTY_AUTH_TOKEN,
        'street': street,
        'city': city,
        'state': state,
        'zipcode': zipcode,
    }

    response = requests.get("https://us-street.api.smarty.com/street-address", params=params)
    
    if response.status_code != 200:
        return False

    data = response.json()
    if len(data) == 0:
        return False
    else:
        return True

def providerList():
    providers = [
    {
        "name": "Dr. Sandra Lee",
        "specialty": "Internal Medicine",
        "location": "Downtown Medical Center",
        "available_times": [
            "Monday"
            "Tuesday"
        ]
    },
    {
        "name": "Dr. Marcus Chen",
        "specialty": "Family Medicine",
        "location": "Westside Clinic",
        "available_times": [
            "Wednesday",
            "Thursday",
        ]
    },
    {
        "name": "Dr. Priya Desai",
        "specialty": "Urgent Care",
        "location": "Uptown Health Hub",
        "available_times": [
            "Friday"
        ]
    }]
    return providers