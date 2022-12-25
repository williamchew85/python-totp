import base64
import hashlib
import hmac
import time

def generate_otp(secret):
  """Generates a TOTP for the given secret."""
  interval = int(time.time()) // 30
  secret_bytes = base64.b32decode(secret)
  msg = struct.pack(">Q", interval)
  h = hmac.new(secret_bytes, msg, hashlib.sha1).digest()
  offset = h[-1] & 0xf
  code = ((h[offset] & 0x7f) << 24 |
          (h[offset + 1] & 0xff) << 16 |
          (h[offset + 2] & 0xff) << 8 |
          (h[offset + 3] & 0xff))
  return str(code % 10**6).zfill(6)

def verify_otp(otp, secret):
  """Verifies a TOTP for the given secret."""
  for i in [-1, 0, 1]:
    if generate_otp(secret, interval=int(time.time()) // 30 + i) == otp:
      return True
  return False
