# def send_email(to, subject, body):
#     print(f"Connecting to SMTP server...")
#     print(f"Sending email to {to} with subject '{subject}'...")
#     print(f"Email sent.")

# def send_sms(to, message):
#     print(f"Connecting to SMS gateway...")
#     print(f"Sending SMS to {to} with message '{message}'...")
#     print(f"SMS sent.")

def send_message(to, connection_message, send_message, message_type):
    print(connection_message)
    print(f"Sending {message_type} to {to} with message '{send_message}'...")
    print(f"{message_type} sent.")

def send_email(to, subject, body):
    send_message(to, "Connecting to SMTP server...", f"with subject '{subject}'...", "Email")

def send_sms(to, message):
    send_message(to, "Connecting to SMS gateway...", message, "SMS")

