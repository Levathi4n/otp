import requests
import random as r

def otp():
  url = '' #your webhook discord
  otp = r.randint(50, 250) + r.randint(70,120)
  data = {
    "username" : "OTP Logs",
    "content" : f"{otp}"
}

  result = requests.post(url, json = data)
  otps = input("Verification code : ")
  if otps == otp:
    print("Correct")
    pass
  else:
    exit()
