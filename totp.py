# This code imports the TOTP class from the totp module and creates a TOTP object with the secret passed from Node.js. 
# It then calls the generate() method on the totp object to generate the OTP, and prints the OTP to stdout.

# Make sure that the totp.py script is in the same directory as the totp.py module that contains the TOTP class, or that the module is importable from the sys.path in the totp.py script.import json
import sys

from totp import TOTP

# Read the data from stdin
data = json.loads(sys.stdin.read())
secret = data['secret']

# Create a TOTP object
totp = TOTP(secret)

# Generate the OTP
otp = totp.generate()

# Send the OTP to stdout
print(otp)
