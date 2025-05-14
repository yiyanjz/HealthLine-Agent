# HealthLine-Agent
This project is a working demo of a conversational AI phone agent designed to streamline new patient intake for medical practices. The system answers a phone number and intelligently guides the caller through a series of questions to collect all necessary information for scheduling a medical appointment.

# Getting Started
- git clone this repo
- cd HealthLine-Agent

# Install Dependencies
- pip3 install Python
- pip3 install Flask
- pip3 install Twilio
- pip3 install Sendgrid
- pip3 install Python
- pip3 install requests
- brew install ngrok

# Set Environment Variables
- SENDGRID_API_KEY=your_sendgrid_api_key
- SMARTY_AUTH_ID=your_smarty_auth_id
- SMARTY_AUTH_TOKEN=your_smarty_auth_token
- TWILIO_ACCOUNT_ID=your_twilio_account_id
- TWILIO_AUTH_TOKEN=your_twilio_auth_token
- TWILIO_NUMBER=your_twilio_number

# Summary and Take-Aways of this project
- For front-end workflow I choose to use a third-party API called Vapi AI and used it to commucated with my back-end file called api.py.
- For back-end I used ngrok which allows me to run python local but using ngrok a tool that allows me to expose a local server (running on your computer or a private network) to the internet through a secure tunnel.
- ngrok config add-authtoken <token>
- ngrok http http://localhost:your_running_port


# Changes I would make
The only issue with this model is the slightly inaccurate collection of user email addresses, due to precision limitations. A reliable solution is to integrate Twilio to send an SMS to the user, allowing them to manually input the required information. This data can then be retrieved through a webhook, significantly improving the accuracy of the collected information.

# Things I would prevent
I do not recommend using VAPI AI for front-end workflow development due to their ongoing and unpredictable changes to available nodes. The current workflow includes nodes like "Say" and "Gather" — where the "Say" node facilitates communication with the user, and the "Gather" node collects input to be passed to an API node (as shown in the image below). However, VAPI frequently makes unannounced changes, removing or modifying key nodes without any documentation or notice. Even their AI assistant is often unaware of these updates.
Because of the instability caused by these constant changes — including the removal of essential nodes like "Say" and "Gather" — VAPI AI proves to be an unreliable platform for building AI agents. For this reason, I strongly advise against using it for any serious development work.

<img width="241" alt="Screenshot 2025-05-14 at 3 24 14 PM" src="https://github.com/user-attachments/assets/97870fd3-f1b7-41b3-9533-a47837179ecf" />
<img width="773" alt="Screenshot 2025-05-14 at 3 24 55 PM" src="https://github.com/user-attachments/assets/903039a6-931f-4050-a2c3-2e0f8e88ffcb" />


Hosted Phone Number
- +1 (239) 264 1967


<img width="329" alt="Screenshot 2025-05-14 at 3 09 15 PM" src="https://github.com/user-attachments/assets/c406ab81-37c0-40a6-8a4b-2806197d7885" />


Below is the workflow I create on VAPI:
- Video availble in files

<img width="1193" alt="Screenshot 2025-05-14 at 3 25 07 PM" src="https://github.com/user-attachments/assets/f149cc52-7dc0-406d-983a-7c4b752ce148" />
<img width="1191" alt="Screenshot 2025-05-14 at 3 25 26 PM" src="https://github.com/user-attachments/assets/d4d0da37-12dc-47aa-a192-1fcb50c2918d" />
<img width="1193" alt="Screenshot 2025-05-14 at 3 28 25 PM" src="https://github.com/user-attachments/assets/8238544b-35de-41f4-9fd0-8ad82056a69d" />
<img width="1189" alt="Screenshot 2025-05-14 at 3 28 43 PM" src="https://github.com/user-attachments/assets/5ef1bc41-6034-477a-b337-c02c549cd26e" />
<img width="1191" alt="Screenshot 2025-05-14 at 3 29 00 PM" src="https://github.com/user-attachments/assets/d4d41054-c2ba-45c2-86f0-beb3a0d93993" />
<img width="1194" alt="Screenshot 2025-05-14 at 3 29 47 PM" src="https://github.com/user-attachments/assets/d378bea6-6778-4fe7-b683-69500b365664" />
<img width="1196" alt="Screenshot 2025-05-14 at 3 30 49 PM" src="https://github.com/user-attachments/assets/b913ca7b-edbe-4abb-855e-b3c6c20d0783" />

