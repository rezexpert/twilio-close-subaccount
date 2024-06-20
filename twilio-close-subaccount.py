import os
from dotenv import load_dotenv
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException

# Load environment variables from .env file
load_dotenv()

# Get the Account SID and Auth Token from environment variables
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")

# Prompt for the sub-account SID
sub_account_sid = input("Please enter the sub-account SID: ")

# Initialize the Twilio client
client = Client(account_sid, auth_token)

try:
    # Update the sub-account status to "closed"
    account = client.api.v2010.accounts(sub_account_sid).update(status="closed")

    # Print success message with friendly_name
    print(f"The subaccount {account.friendly_name} has been closed.")
except TwilioRestException as e:
    # Print error message
    print(f"Error: {e}")
