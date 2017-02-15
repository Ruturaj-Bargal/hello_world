from twilio.rest import TwilioRestClient

account_sid = "AC6522ee0f8ae923603238bf5a118cd308" # Your Account SID from www.twilio.com/console
auth_token  = "8c2cfa202b07786d7d62e6dc5993e3cd"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(
    body="My name is Ruturaj Bargal",
    to="+919003222077",    # Replace with your phone number
    from_="+18305492004") # Replace with your Twilio number

print(message.sid)
