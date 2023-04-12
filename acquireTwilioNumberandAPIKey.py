# Import the Client class from the Twilio library
from twilio.rest import Client

# Replace these variables with your Twilio account SID and auth token
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'

# Replace this variable with your desired area code for the phone number
area_code = 'your_area_code'

# Initialize the Twilio Client with your account SID and auth token
client = Client(account_sid, auth_token)

# Search for available Twilio phone numbers in the specified area code
# and store the result as a list of numbers
available_numbers = client.available_phone_numbers('US').local.list(area_code=area_code)

# Get the first available phone number from the list
new_number = available_numbers[0].phone_number

# Purchase the selected phone number using the Twilio Client
purchased_number = client.incoming_phone_numbers.create(phone_number=new_number)

# Print the purchased Twilio phone number to the console
print(f"Purchased Twilio phone number: {purchased_number.phone_number}")

# Create a new Twilio API key with a friendly name and store the result as an API key object
api_key = client.api.keys.create(friendly_name='My API Key')

# Print the API Key SID to the console
print(f"API Key SID: {api_key.sid}")

# Print the API Key Secret to the console
print(f"API Key Secret: {api_key.secret}")
