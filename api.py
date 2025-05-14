from flask import Flask, jsonify, request
from helper import validate_address_smartystreets, providerList
import sendgrid
import os
from sendgrid.helpers.mail import Mail, Email, To, Content
from datetime import datetime
from sendgrid import SendGridAPIClient
import certifi
from dotenv import load_dotenv
from twilio.rest import Client

app = Flask(__name__)

# Load .env file
load_dotenv()

# grab sendgrid keys
sendgrid_api_key = os.environ.get("SENDGRID_API_KEY")
if not sendgrid_api_key:
    raise ValueError("SENDGRID_API_KEY is not set in environment variables.")
os.environ['SSL_CERT_FILE'] = certifi.where()

# grab twillo keys
twilio_account_id = os.environ.get("TWILIO_ACCOUNT_ID")
twilio_auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
twilio_phone_number = os.environ.get("TWILIO_NUMBER")
client = Client(twilio_account_id, twilio_auth_token)

# an API used to validate if provided address is valid
@app.route('/checks_address', methods=["POST"])
def checks_address():
    address = request.get_json()
    if not address:
        return jsonify({"error": "Invalid JSON."}), 400

    # validate address through smartystreets
    is_valid = validate_address_smartystreets(
        address['streetAddress'],
        address['city'],
        address['state'],
        address['zipCode']
    )

    if is_valid:
        return jsonify({"valid_address": True})
    else:
        return jsonify({"valid_address": False})


# an API used to return doctor's and available times
@app.route('/returns_doctor_time', methods=["POST"])
def get_doctors_times():
    appointment = request.get_json()
    provider_name = ""

    # grab providers list
    providers_list = providerList()
    for provider in providers_list:
        available_times = provider["available_times"]
        if appointment['appointmentDay'] in available_times:
            provider_name = provider['name']

    return jsonify({"doctorName": provider_name, "doctorTime": appointment['appointmentTime']})


# an API that aggregates all the availbe data and send the patient an email
@app.route('/send_email', methods=["POST"])
def send_email():
    # input data
    data = request.get_json()

    # Dictionary to send
    send_data = {
        'Patient Name': data['patientName'],
        'Patient Date of Birth': data['patientDOB'],
        'Patient Insurance Provider': data['insuranceProvider'],
        'Patient Scheduled Appointment Time': data['appointmentTime'],
        'Patient Scheduled Appointment Day': data['appointmentDay'],
        'Patient Reason for Visit': data['visitReason'],
        'Patient Physician Name': data['doctorName'],
    }
    patient_email = data['email']

    if patient_email:
        # Convert dictionary to a readable string
        body = "\n".join(f"{key}: {value}" for key, value in send_data.items())

        # Email details
        from_email = "yiyanzhangcoding@gmail.com"
        to_email = patient_email
        now = datetime.now()
        date_string = now.strftime("%Y-%m-%d")
        subject = f"Confirmation: Appointment Scheduled on {date_string}"

        # Create the email message
        message = Mail(
            from_email=from_email,
            to_emails=to_email,
            subject=subject,
            plain_text_content=body
        )

        # Send the email
        try:
            sg = SendGridAPIClient(sendgrid_api_key)
            response = sg.send(message)
            print(f"Email sent! Status Code: {response.status_code}")
            print(response.body)
            print(response.headers)
            return jsonify({"call_completed": True})
        except Exception as e:
            print(f"An error occurred: {e}")
            return jsonify({"call_completed": False})
    else:
        return jsonify({"call_completed": True})

if __name__ == "__main__":
    app.run(debug=True)