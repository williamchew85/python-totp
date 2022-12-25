# python-totp
Time-Based One-Time Password (TOTP) with Python

This code uses the hmac and hashlib libraries to generate a TOTP based on the current time interval and a shared secret. The generate_otp() function takes a secret as input and returns a 6-digit OTP. The verify_otp() function takes an OTP and a secret as input and returns True if the OTP is correct and False if it is not.

You will need to replace the secret with a secret that is shared between the server and the client (e.g. a user's phone number). You can then use the generate_otp() function to generate an OTP and send it to the user, and use the verify_otp() function to verify the OTP when it is entered by the user.
