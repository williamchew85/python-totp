# Generate an OTP
otp = generate_otp(secret)

# Send the OTP to the client
# (e.g. via SMS or email)

# The client enters the OTP into the app
entered_otp = input("Enter the OTP: ")

# Verify the OTP
if verify_otp(entered_otp, secret):
  print("OTP verified!")
else:
  print("Invalid OTP")
