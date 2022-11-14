from preferences import Preferences
import smtplib, ssl

preferences = Preferences()

port = 465  # For SSL
password = preferences.password  if preferences.preferences is not None else input("Type your password and press enter: ")

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(preferences.email, password)
    # TODO: Send email here